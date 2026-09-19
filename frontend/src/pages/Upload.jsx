import { useRef, useState } from 'react'
import { useNavigate } from 'react-router-dom'

import Navbar from '../components/layout/Navbar'
import Footer from '../components/layout/Footer'
import CameraCapture from '../components/camera/CameraCapture'
import { detectDisease } from '../services/detectionService'

import './Upload.css'

function Upload() {
  const navigate = useNavigate()
  const fileInputRef = useRef(null)
  const cameraInputRef = useRef(null)

  const [image, setImage] = useState(null)
  const [preview, setPreview] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [showCamera, setShowCamera] = useState(false)

  // Shared by gallery selection and camera capture (live or fallback).
  function applyImageFile(file) {
    if (!file.type.startsWith('image/')) {
      setError('File harus berupa gambar.')
      return
    }

    if (preview) {
      URL.revokeObjectURL(preview)
    }

    const imageUrl = URL.createObjectURL(file)

    setError('')
    setImage(file)
    setPreview(imageUrl)
  }

  // Handle image selection from the gallery file input.
  function handleFileChange(event) {
    const file = event.target.files?.[0]
    if (!file) return
    applyImageFile(file)
  }

  // "Gunakan Kamera" button: try a live in-browser camera first (works on
  // desktop webcams and on mobile over HTTPS/localhost). If getUserMedia
  // isn't available — e.g. testing from a phone over a plain-HTTP LAN
  // address — fall back to the native OS camera via the hidden file input,
  // which has no secure-context requirement.
  function openCamera() {
    if (navigator.mediaDevices?.getUserMedia) {
      setShowCamera(true)
    } else {
      cameraInputRef.current?.click()
    }
  }

  function handleCameraCapture(file) {
    applyImageFile(file)
    setShowCamera(false)
  }

  function handleCameraUnavailable() {
    setShowCamera(false)
    cameraInputRef.current?.click()
  }

  // Fallback native camera input (mobile browsers, or when getUserMedia fails).
  function handleCameraInputChange(event) {
    const file = event.target.files?.[0]
    if (!file) return
    applyImageFile(file)
  }

  // Remove the selected image and reset the file input.
  function handleRemoveImage() {
    if (preview) {
      URL.revokeObjectURL(preview)
    }

    setImage(null)
    setPreview(null)

    // Allow the same file to be selected again.
    if (fileInputRef.current) {
      fileInputRef.current.value = ''
    }
  }

  // Run disease detection and save the result to history.
  async function handleDetect() {
    if (!image) {
      setError('Silakan pilih foto terlebih dahulu.')
      return
    }

    try {
      setLoading(true)
      setError('')

      // Backend saves the scan (and its history entry) itself —
      // no separate save step needed on the frontend anymore.
      const result = await detectDisease(image)

      navigate('/result', {
        state: {
          result,
        },
      })
    } catch (err) {
      console.error(err)
      if (err.isUncertain) {
        setError(err.message)
      } else {
        const detail = err.response?.data?.error
        setError(
          detail || 'Terjadi kesalahan saat melakukan deteksi.'
        )
      }
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <Navbar />

      <main className="page">
        <section className="upload-section">
          <div className="container">
            <div>
                <h1>Deteksi Penyakit Padi</h1>

                <p>
                  Analisis cerdas berbasis AI untuk mendeteksi penyakit pada daun padi secara akurat.
                </p>
              </div>

            {/* Upload options */}
            {!preview && (
              <div className="upload-options">
                <label className="upload-box">
                  <span>📁</span>
                  <strong>Pilih dari Galeri</strong>
                  <small>JPG, JPEG, PNG</small>

                  <input
                    ref={fileInputRef}
                    type="file"
                    accept="image/*"
                    onChange={handleFileChange}
                  />
                </label>

                <button
                  type="button"
                  className="upload-box"
                  onClick={openCamera}
                >
                  <span>📷</span>
                  <strong>Gunakan Kamera</strong>
                  <small>Ambil foto langsung</small>
                </button>

                {/* Fallback for mobile / when the live camera can't start */}
                <input
                  ref={cameraInputRef}
                  type="file"
                  accept="image/*"
                  capture="environment"
                  onChange={handleCameraInputChange}
                  style={{ display: 'none' }}
                />
              </div>
            )}

            {/* Image preview and actions */}
            {preview && (
              <div className="preview-container">
                <img
                  src={preview}
                  alt="Preview daun padi"
                  className="image-preview"
                />

                <button
                  type="button"
                  className="secondary-button"
                  onClick={handleRemoveImage}
                  disabled={loading}
                >
                  Pilih Foto Lain
                </button>

                <button
                  type="button"
                  className="primary-button"
                  onClick={handleDetect}
                  disabled={loading}
                >
                  {loading
                    ? 'Sedang Menganalisis...'
                    : 'Deteksi Penyakit'}
                </button>
              </div>
            )}

            {/* Error message */}
            {error && (
              <p className="error-message">
                {error}
              </p>
            )}
          </div>
        </section>
      </main>

      {showCamera && (
        <CameraCapture
          onCapture={handleCameraCapture}
          onClose={() => setShowCamera(false)}
          onUnavailable={handleCameraUnavailable}
        />
      )}

      <Footer />
    </>
  )
}

export default Upload