import { useEffect, useRef, useState } from 'react'
import './CameraCapture.css'

function CameraCapture({ onCapture, onClose, onUnavailable }) {
  const videoRef = useRef(null)
  const canvasRef = useRef(null)
  const streamRef = useRef(null)

  const [error, setError] = useState('')
  const [capturedUrl, setCapturedUrl] = useState(null)

  useEffect(() => {
    let cancelled = false

    async function startCamera() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          video: { facingMode: 'environment' },
          audio: false,
        })

        if (cancelled) {
          stream.getTracks().forEach((track) => track.stop())
          return
        }

        streamRef.current = stream
        if (videoRef.current) {
          videoRef.current.srcObject = stream
        }
      } catch (err) {
        console.error('Camera unavailable:', err)
        if (!cancelled) {
          onUnavailable()
        }
      }
    }

    startCamera()

    return () => {
      cancelled = true
      streamRef.current?.getTracks().forEach((track) => track.stop())
    }

  }, [])

  function handleCapture() {
    const video = videoRef.current
    const canvas = canvasRef.current
    if (!video || !canvas) return

    canvas.width = video.videoWidth
    canvas.height = video.videoHeight
    canvas.getContext('2d').drawImage(video, 0, 0)

    canvas.toBlob((blob) => {
      if (!blob) {
        setError('Gagal mengambil foto. Coba lagi.')
        return
      }
      setCapturedUrl(URL.createObjectURL(blob))
    }, 'image/jpeg', 0.9)
  }

  function handleRetake() {
    if (capturedUrl) URL.revokeObjectURL(capturedUrl)
    setCapturedUrl(null)
  }

  function handleUsePhoto() {
    const canvas = canvasRef.current
    canvas.toBlob((blob) => {
      if (!blob) return
      const file = new File([blob], `camera-${Date.now()}.jpg`, { type: 'image/jpeg' })
      onCapture(file)
    }, 'image/jpeg', 0.9)
  }

  function handleClose() {
    streamRef.current?.getTracks().forEach((track) => track.stop())
    if (capturedUrl) URL.revokeObjectURL(capturedUrl)
    onClose()
  }

  return (
    <div className="camera-modal-backdrop" onClick={handleClose}>
      <div className="camera-modal" onClick={(e) => e.stopPropagation()}>
        <div className="camera-modal-header">
          <h3>Ambil Foto Daun Padi</h3>
          <button type="button" className="camera-close-button" onClick={handleClose}>
            ✕
          </button>
        </div>

        <div className="camera-viewport">
          {}
          <video
            ref={videoRef}
            autoPlay
            playsInline
            muted
            style={{ display: capturedUrl ? 'none' : 'block' }}
          />

          {}
          {capturedUrl && (
            <img src={capturedUrl} alt="Foto yang diambil" className="camera-captured-preview" />
          )}

          <canvas ref={canvasRef} style={{ display: 'none' }} />
        </div>

        {error && <p className="error-message">{error}</p>}

        <div className="camera-modal-actions">
          {!capturedUrl ? (
            <button type="button" className="primary-button" onClick={handleCapture}>
              📷 Ambil Foto
            </button>
          ) : (
            <>
              <button type="button" className="secondary-button" onClick={handleRetake}>
                Ambil Ulang
              </button>
              <button type="button" className="primary-button" onClick={handleUsePhoto}>
                Gunakan Foto Ini
              </button>
            </>
          )}
        </div>
      </div>
    </div>
  )
}

export default CameraCapture
