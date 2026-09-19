import api from './api'

// POST /auth/register/ -> creates the account and logs them in immediately
// (backend returns access + refresh tokens on register, same as login).
export async function register({ fullName, email, password, confirmPassword }) {
  const { data } = await api.post('/auth/register/', {
    full_name: fullName,
    email,
    password,
    confirm_password: confirmPassword,
  })
  storeSession(data)
  return data.user
}

// POST /auth/login/
export async function login({ email, password }) {
  const { data } = await api.post('/auth/login/', { email, password })
  localStorage.setItem('access_token', data.access)
  localStorage.setItem('refresh_token', data.refresh)

  const user = await getMe()
  localStorage.setItem('user', JSON.stringify(user))
  return user
}

// GET /auth/me/
export async function getMe() {
  const { data } = await api.get('/auth/me/')
  return data
}

export function logout() {
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  localStorage.removeItem('user')
}

export function getStoredUser() {
  const raw = localStorage.getItem('user')
  return raw ? JSON.parse(raw) : null
}

export function isAuthenticated() {
  return Boolean(localStorage.getItem('access_token'))
}

function storeSession(data) {
  localStorage.setItem('access_token', data.access)
  localStorage.setItem('refresh_token', data.refresh)
  localStorage.setItem('user', JSON.stringify(data.user))
}
