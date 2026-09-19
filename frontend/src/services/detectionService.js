import api from './api'

// POST /detections/ — upload a leaf photo and get the diagnosis back.
// Requires auth (handled automatically by api.js's request interceptor).
//
// Maps the backend's nested shape:
//   { id, image, disease: { name, slug, short_description, risk_level }, confidence, inference_time_ms, created_at }
// into the flat shape the existing pages (Result.jsx, History.jsx) expect.
export async function detectDisease(imageFile) {
  const formData = new FormData()
  formData.append('image', imageFile)

  const { data } = await api.post('/detections/', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })

  // Model wasn't confident enough — backend doesn't save this as history.
  // Surface it distinctly so Upload.jsx can prompt a retake instead of
  // navigating to a Result page with no disease/id to show.
  if (data.is_uncertain) {
    const err = new Error(data.message)
    err.isUncertain = true
    err.confidence = data.confidence
    throw err
  }

  return mapDetection(data)
}

export function mapDetection(data) {
  return {
    id: data.id,
    disease_name: data.disease.name,
    disease_slug: data.disease.slug,
    confidence: data.confidence,
    description: data.disease.short_description,
    risk_level: data.disease.risk_level,
    image_url: data.image,
    created_at: data.created_at,
  }
}
