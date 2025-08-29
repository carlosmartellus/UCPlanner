import MenuButton from './MenuButton'

export default function Menu({ setView, user, handleLogout }) {
  return (
    <div className="menu">
      <MenuButton onClick={() => setView('register')}>Registrarse</MenuButton>
      <MenuButton onClick={() => setView('login')}>Login</MenuButton>
      <MenuButton onClick={() => setView('settings')}>Configuración</MenuButton>
      {user && <MenuButton onClick={handleLogout}>Salir</MenuButton>}
    </div>
  )
}
