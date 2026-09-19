import { Routes, Route } from 'react-router-dom'

import Home from './pages/Home'
import Upload from './pages/Upload'
import Result from './pages/Result'
import History from './pages/History'
import DiseaseList from './pages/DiseaseList'
import DiseaseDetail from './pages/DiseaseDetail'
import Login from './pages/Login'
import Register from './pages/Register'

import ScrollToHash from './components/common/ScrollToHash'
import ProtectedRoute from './components/common/ProtectedRoute'

function App() {
  return (
    <>
      {/* Handle navigation to sections using URL hashes */}
      <ScrollToHash />

      {/* Application routes */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* These require a logged-in user, since the backend's
            /detections/ endpoints are authenticated. */}
        <Route
          path="/upload"
          element={
            <ProtectedRoute>
              <Upload />
            </ProtectedRoute>
          }
        />
        <Route
          path="/result"
          element={
            <ProtectedRoute>
              <Result />
            </ProtectedRoute>
          }
        />
        <Route
          path="/history"
          element={
            <ProtectedRoute>
              <History />
            </ProtectedRoute>
          }
        />

        {/* Public — disease catalog doesn't need login */}
        <Route path="/diseases" element={<DiseaseList />} />
        <Route
          path="/diseases/:id"
          element={<DiseaseDetail />}
        />
      </Routes>
    </>
  )
}

export default App
