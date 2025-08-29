import { useState, useEffect } from 'react'
import './Home.css'
import Menu from './menu/Menu'
import RegisterForm from './menu/RegisterForm'
import UsersList from './menu/UsersList'
import Settings from './menu/Settings'

function Home({ user, setUser, setAppView }) {
  const [view, setView] = useState('home')
  const [nameInput, setNameInput] = useState('')
  const [usersList, setUsersList] = useState([])

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
    setAppView('home')
  }

  return (
    <div className="Home">
      <h1>Bienvenid@ a UCPlanner!</h1>

      {view === 'home' && (
        <Menu
          setView={setView}
          user={user}
          handleLogout={handleLogout}
          setAppView={setAppView}
        />
      )}

      {view === 'register' && (
        <RegisterForm
          nameInput={nameInput}
          setNameInput={setNameInput}
          setView={setView}
          setUser={setUser}
          setAppView={setAppView}
        />
      )}

      {view === 'login' && (
        <UsersList
          usersList={usersList}
          setUser={setUser}
          setView={setView}
          setAppView={setAppView}
        />
      )}

      {view === 'settings' && <Settings setView={setView} />}

      {user && <p>Hola, {user.name}</p>}
    </div>
  )
}

export default Home
