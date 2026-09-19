import { useState } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom'

import Navbar from '../components/layout/Navbar'
import Footer from '../components/layout/Footer'
import { useAuth } from '../context/AuthContext'

import './Auth.css'

function Login() {
  const { login, loading } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()

  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  async function handleSubmit(event) {
    event.preventDefault()
    setError('')

    try {
      await login({ email, password })
      const redirectTo = location.state?.from?.pathname || '/upload'
      navigate(redirectTo, { replace: true })
    } catch (err) {
      const detail = err.response?.data?.detail
      setError(detail || 'Email atau password salah.')
    }
  }

  return (
    <>
      <Navbar />

      <main className="page">
        <section className="auth-section">
          <div className="auth-card">
            <h1>Login ke Akunmu</h1>
            <p>Masuk untuk mulai mendeteksi penyakit daun padi.</p>

            <form onSubmit={handleSubmit} className="auth-form">
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
                  required
                />
              </label>

              {error && <p className="error-message">{error}</p>}

              <button type="submit" className="primary-button" disabled={loading}>
                {loading ? 'Masuk...' : 'Masuk'}
              </button>
            </form>

            <p className="auth-switch">
              Belum punya akun? <Link to="/register">Daftar Akun</Link>
            </p>
          </div>
        </section>
      </main>

      <Footer />
    </>
  )
}

export default Login
