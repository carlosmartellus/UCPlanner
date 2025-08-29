import MenuButton from './MenuButton'

export default function RegisterForm({ nameInput, setNameInput, setView, setUser, setAppView }) {
  const handleRegisterSubmit = async () => {
    if (!nameInput.trim()) {
      console.log('Cannot send empty name')
      return
    }

    const res = await fetch('http://127.0.0.1:8000/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: nameInput })
    })

    if (res.status === 400) {
      alert('El usuario ya existe')
      return
    }

    if (res.status >= 500) {
      alert('Error del servidor, intente más tarde')
      return
   }

    const newUser = await res.json()
    setUser(newUser)
    setNameInput('')
    setAppView('user')
  }

  return (
    <div className="form">
      <input
        type="text"
        placeholder="Ingresa tu nombre"
        value={nameInput}
        onChange={(e) => setNameInput(e.target.value)}
      />
      <MenuButton onClick={handleRegisterSubmit}>Enviar</MenuButton>
      <MenuButton onClick={() => setView('home')}>Volver</MenuButton>
    </div>
  )
}
