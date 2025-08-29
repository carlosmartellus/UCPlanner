// UsersList.jsx
import { useState, useEffect } from 'react'
import MenuButton from './MenuButton'

export default function UsersList({ setUser, setView }) {
  const [usersList, setUsersList] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const res = await fetch('http://127.0.0.1:8000/users/')
        if (!res.ok) throw new Error('Error al cargar usuarios')
        const data = await res.json()
        setUsersList(data)
      } catch (err) {
        console.error(err)
        alert('No se pudieron cargar los usuarios')
      } finally {
        setLoading(false)
      }
    }

    fetchUsers()
  }, [])

  if (loading) return <p>Cargando usuarios...</p>
  if (!usersList.length) {
    return (
      <div className="users-list">
        <h2>No hay usuarios registrados</h2>
        <MenuButton onClick={() => setView('home')}>Volver</MenuButton>
      </div>
    )
  }

  return (
    <div className="users-list">
      <h2>Usuarios registrados:</h2>
      <div className="users-buttons">
        {usersList.map((u) => (
          <MenuButton
            key={u.id}
            onClick={() => {
              console.log('Usuario clickeado', u.name)
              setUser(u)
              setView('user')
            }}
          >
            {u.name}
          </MenuButton>
        ))}
      </div>
      <MenuButton onClick={() => setView('home')}>Volver</MenuButton>
    </div>
  )
}
