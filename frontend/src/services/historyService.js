import api from './api'
import { mapDetection } from './detectionService'

// GET /detections/  (optionally ?disease=<slug>) — the logged-in user's scan history.
export async function getHistory(diseaseSlug) {
  const params = diseaseSlug ? { disease: diseaseSlug } : {}
  const { data } = await api.get('/detections/', { params })
  return data.map(mapDetection)
}

// DELETE /detections/<id>/ — "Hapus" a single scan.
export async function deleteDetection(id) {
  await api.delete(`/detections/${id}/`)
}
