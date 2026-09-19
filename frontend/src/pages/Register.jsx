import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'

import Navbar from '../components/layout/Navbar'
import Footer from '../components/layout/Footer'
import { useAuth } from '../context/AuthContext'

import './Auth.css'

function Register() {
  const { register, loading } = useAuth()
  const navigate = useNavigate()

  const [fullName, setFullName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [error, setError] = useState('')

  async function handleSubmit(event) {
    event.preventDefault()
    setError('')

    if (password !== confirmPassword) {
      setError('Password dan konfirmasi password tidak cocok.')
      return
    }

    try {
      await register({ fullName, email, password, confirmPassword })
      navigate('/upload', { replace: true })
    } catch (err) {
      // DRF validation errors come back as {field: [messages]}
      const data = err.response?.data
      const firstError = data && Object.values(data)[0]?.[0]
      setError(firstError || 'Gagal membuat akun. Coba lagi.')
    }
  }

  return (
    <>
      <Navbar />

      <main className="page">
        <section className="auth-section">
          <div className="auth-card">
            <h1>Buat Akun Baru</h1>
            <p>Daftar untuk mulai menggunakan HealthyRice.AI.</p>

            <form onSubmit={handleSubmit} className="auth-form">
              <label>
                Nama Lengkap
                <input
                  type="text"
                  value={fullName}
                  onChange={(e) => setFullName(e.target.value)}
                  required
                />
              </label>

              <label>
                Email
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </label>

              <label>
                Password
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  minLength={8}
                  required
                />
              </label>

              <label>
                Konfirmasi Password
                <input
                  type="password"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                  minLength={8}
                  required
                />
              </label>

              {error && <p className="error-message">{error}</p>}

              <button type="submit" className="primary-button" disabled={loading}>
                {loading ? 'Membuat Akun...' : 'Buat Akun'}
              </button>
            </form>

            <p className="auth-switch">
              Sudah punya akun? <Link to="/login">Login</Link>
            </p>
          </div>
        </section>
      </main>

      <Footer />
    </>
  )
}

export default Register
