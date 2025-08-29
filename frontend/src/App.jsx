import { useState } from 'react'
import './App.css'

function App() {
  const [user, setUser] = useState(null)
  const [isRegistering, setIsRegistering] = useState(false)
  const [nameInput, setNameInput] = useState('')

  const handleRegisterClick = () => {
    setIsRegistering(true)
  }

  const handleRegisterSubmit = async () => {
    if (nameInput.trim() === '') return
    try {
      const response = await fetch("http://localhost:8000/users/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name: nameInput }),
      })

      if (!response.ok) {
        throw new Error("Error al registrar usuario")
      }

      const data = await response.json()
      console.log(data)

      setUser({ name: data.name })
      setIsRegistering(false)
      setNameInput('')
    } catch (error) {
      console.error(error)
      alert("No se pudo registrar el usuario")
    }
  }


  const handleLogin = () => {
    console.log('Login seleccionado')
    setUser({ name: 'UsuarioEjemplo' })
  }

  const handleSettings = () => {
    console.log('Configuración seleccionada')
  }

  const handleLogout = () => {
    console.log('Salir seleccionado')
    setUser(null)
  }

  return (
    <div className="App">
      <h1>Bienvenid@ a UCPlanner!</h1>

      {user && <p>Hola, {user.name}</p>}

      <div className="menu">
        <button onClick={handleRegisterClick}>Registrarse</button>
        <button onClick={handleLogin}>Login</button>
        <button onClick={handleSettings}>Configuración</button>
        <button onClick={handleLogout}>Salir</button>
      </div>

      {isRegistering && (
        <div className="register-form">
          <input
            type="text"
            placeholder="Ingresa tu nombre"
            value={nameInput}
            onChange={(e) => setNameInput(e.target.value)}
          />
          <button onClick={handleRegisterSubmit}>Enviar</button>
        </div>
      )}
    </div>
  )
}

export default App
