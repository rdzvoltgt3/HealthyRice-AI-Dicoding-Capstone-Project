import { createContext, useContext, useEffect, useState } from 'react'
import * as authService from '../services/authService'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => authService.getStoredUser())
  const [loading, setLoading] = useState(false)

  // On first load, if we have a token but no cached user (e.g. after a
  // refresh-token-only session), fetch the current user once.
  useEffect(() => {
    if (authService.isAuthenticated() && !user) {
      authService.getMe().then(setUser).catch(() => authService.logout())
    }
  }, [user])

  async function login(credentials) {
    setLoading(true)
    try {
      const loggedInUser = await authService.login(credentials)
      setUser(loggedInUser)
      return loggedInUser
    } finally {
      setLoading(false)
    }
  }

  async function register(fields) {
    setLoading(true)
    try {
      const newUser = await authService.register(fields)
      setUser(newUser)
      return newUser
    } finally {
      setLoading(false)
    }
  }

  function logout() {
    authService.logout()
    setUser(null)
  }

  return (
    <AuthContext.Provider
      value={{ user, loading, isAuthenticated: Boolean(user), login, register, logout }}
    >
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used within an AuthProvider')
  return ctx
}
