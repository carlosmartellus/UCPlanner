import MenuButton from './MenuButton'

export default function Settings({ setView }) {
  return (
    <div className="settings">
      <h2>Configuración</h2>
      <MenuButton onClick={() => setView('home')}>Volver</MenuButton>
    </div>
  )
}
