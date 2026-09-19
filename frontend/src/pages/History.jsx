import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

import Navbar from '../components/layout/Navbar'
import Footer from '../components/layout/Footer'

import { getHistory, deleteDetection } from '../services/historyService'
import { formatDate } from '../utils/format'

import './History.css'

function History() {
  const [history, setHistory] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    loadHistory()
  }, [])

  async function loadHistory() {
    try {
      setLoading(true)
      setError('')
      const data = await getHistory()
      setHistory(data)
    } catch (err) {
      console.error(err)
      setError('Gagal memuat riwayat deteksi.')
    } finally {
      setLoading(false)
    }
  }

  // Delete every item one by one via the backend, then refresh.
  async function handleClear() {
    const confirmed = window.confirm('Hapus semua riwayat deteksi?')
    if (!confirmed) return

    try {
      await Promise.all(history.map((item) => deleteDetection(item.id)))
      setHistory([])
    } catch (err) {
      console.error(err)
      setError('Gagal menghapus riwayat.')
    }
  }

  async function handleDeleteOne(id) {
    try {
      await deleteDetection(id)
      setHistory((prev) => prev.filter((item) => item.id !== id))
    } catch (err) {
      console.error(err)
      setError('Gagal menghapus item ini.')
    }
  }

  return (
    <>
      <Navbar />

      <main className="page">
        <section className="history-section">
          <div className="container">

            {/* Page heading and clear action */}
            <div className="section-header">
              <div>
                <h1>Riwayat Deteksi</h1>

                <p>
                  Hasil deteksi yang pernah kamu lakukan.
                </p>
              </div>

              {history.length > 0 && (
                <button
                  type="button"
                  className="danger-button"
                  onClick={handleClear}
                >
                  Hapus Semua
                </button>
              )}
            </div>

            {error && <p className="error-message">{error}</p>}

            {loading ? (
              <p>Memuat riwayat...</p>
            ) : history.length === 0 ? (
              <div className="empty-state">
                <h3>Belum ada riwayat</h3>

                <p>
                  Hasil deteksi yang kamu lakukan akan muncul
                  di sini.
                </p>

                <Link
                  to="/upload"
                  className="primary-button"
                >
                  Mulai Deteksi
                </Link>
              </div>
            ) : (
              /* Detection history */
              <div className="history-list">
                {history.map((item) => (
                  <article
                    className="history-card"
                    key={item.id}
                  >
                    {item.image_url && (
                      <img
                        src={item.image_url}
                        alt={`Hasil deteksi ${item.disease_name}`}
                      />
                    )}

                    <div className="history-card-content">
                      <h3>{item.disease_name}</h3>

                      <p>
                        Confidence: {item.confidence}%
                      </p>

                      <small>
                        {formatDate(item.created_at)}
                      </small>
                    </div>

                    <Link
                      to={`/diseases/${item.disease_slug}`}
                      className="history-card-link"
                    >
                      Detail
                    </Link>

                    <button
                      type="button"
                      className="danger-button"
                      onClick={() => handleDeleteOne(item.id)}
                    >
                      Hapus
                    </button>
                  </article>
                ))}
              </div>
            )}

          </div>
        </section>
      </main>

      <Footer />
    </>
  )
}

export default History
