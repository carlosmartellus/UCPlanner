export default function MenuButton({ onClick, children }) {
  return (
    <button type="button" onClick={onClick}>
      {children}
    </button>
  )
}
