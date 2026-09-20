import json
import logging
import time
from pathlib import Path

import numpy as np
import onnxruntime as ort
from PIL import Image

logger = logging.getLogger(__name__)

ASSETS_DIR = Path(__file__).parent / "ml_assets"

_CFG = json.loads((ASSETS_DIR / "preprocess_config.json").read_text())
_LABELS = json.loads((ASSETS_DIR / "labels.json").read_text())
_CLASSES = _LABELS["classes"]

_REJECT_LABELS = set(_LABELS.get("reject_labels", []))
_CROP_SIZE = _CFG["center_crop"]
_RESIZE_SHORTER = _CFG["resize_shorter_side_to"]
_THRESHOLD = _CFG["confidence_threshold"]

_session = ort.InferenceSession(
    str(ASSETS_DIR / "model_web_int8.onnx"),
    providers=["CPUExecutionProvider"],
)
_INPUT_NAME = _session.get_inputs()[0].name
_OUTPUT_SIZE = _session.get_outputs()[0].shape[-1]

if _OUTPUT_SIZE != len(_CLASSES):

    logger.warning(
        "ml_engine: model outputs %d classes but labels.json lists %d (%s). "
        "Classes beyond index %d can never be predicted until the model is updated.",
        _OUTPUT_SIZE, len(_CLASSES), _CLASSES, _OUTPUT_SIZE - 1,
    )


def _preprocess(image_path: str) -> np.ndarray:
    img = Image.open(image_path).convert("RGB")
    w, h = img.size
    scale = _RESIZE_SHORTER / min(w, h)
    img = img.resize((round(w * scale), round(h * scale)), Image.BILINEAR)
    left = (img.width - _CROP_SIZE) // 2
    top = (img.height - _CROP_SIZE) // 2
    img = img.crop((left, top, left + _CROP_SIZE, top + _CROP_SIZE))
    arr = np.asarray(img, dtype=np.float32) / 255.0
    # (1, 3, H, W)
    return np.transpose(arr, (2, 0, 1))[None].astype(np.float32)


def _normalize_label(raw_label: str) -> str:

    return raw_label.replace("_", "-")


def run_inference(image_path: str) -> dict:

    start = time.time()

    x = _preprocess(image_path)
    probs = _session.run(None, {_INPUT_NAME: x})[0][0]

    idx = int(np.argmax(probs))
    raw_label = _CLASSES[idx]
    label = _normalize_label(raw_label)
    confidence = float(probs[idx]) * 100

    is_rejected = raw_label in _REJECT_LABELS
    is_low_confidence = probs[idx] < _THRESHOLD
    is_uncertain = is_rejected or is_low_confidence

    if is_rejected:
        reason = "not_rice" if raw_label == "not_rice" else "rejected_class"
        message = "Foto ini sepertinya bukan daun padi. Mohon foto daun padi yang jelas."
    elif is_low_confidence:
        reason = "low_confidence"
        message = "Model kurang yakin. Mohon foto ulang daun dari jarak dekat dengan pencahayaan cukup."
    else:
        reason = None
        message = "Deteksi berhasil."

    inference_time_ms = int((time.time() - start) * 1000)

    return {
        "label": label,
        "confidence": round(confidence, 2),
        "inference_time_ms": inference_time_ms,
        "is_uncertain": is_uncertain,
        "reason": reason,
        "message": message,
    }
