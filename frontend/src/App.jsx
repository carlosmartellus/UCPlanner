import { useState, useEffect } from 'react'
import './App.css'
import Menu from './menu/Menu'
import RegisterForm from './menu/RegisterForm'
import UsersList from './menu/UsersList'
import Settings from './menu/Settings'

function App() {
  const [view, setView] = useState('home')
  const [user, setUser] = useState(null)
  const [nameInput, setNameInput] = useState('')

  useEffect(() => {
    if (view === 'login') {
      fetch('http://127.0.0.1:8000/users/')
        .then((res) => res.json())
        .then((data) => setUsersList(data))
        .catch((err) => console.error('Error cargando usuarios:', err))
    }
  }, [view])

  const handleLogout = () => {
    setUser(null)
    setView('home')
  }

  return (
    <div className="App">
      <h1>Bienvenid@ a UCPlanner!</h1>

      {view === 'home' && (
        <Menu
          setView={setView}
          user={user}
          handleLogout={handleLogout}
        />
      )}

      {view === 'register' && (
        <RegisterForm
          nameInput={nameInput}
          setNameInput={setNameInput}
          setView={setView}
          setUser={setUser}
        />
      )}

      {view === 'login' && (
        <UsersList
        setUser={setUser}
        setView={setView}
        />
      )}

      {view === 'settings' && <Settings setView={setView} />}

      {user && <p>Hola, {user.name}</p>}
    </div>
  )
}

export default App
