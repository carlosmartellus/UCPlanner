import { useState, useEffect } from 'react'

function User({
  user,
  degreeNameInput,
  setDegreeNameInput,
  schoolInput,
  setSchoolInput,
  creditInput,
  setCreditInput
}) {
  const [userDegrees, setUserDegrees] = useState([])

  useEffect(() => {
    if (!user) return

    const fetchDegrees = async () => {
      try {
        const res = await fetch(`http://127.0.0.1:8000/user-degrees/${user.id}`)
        if (!res.ok) throw new Error('Error al cargar las carreras del usuario')
        const data = await res.json()
        setUserDegrees(data)
      } catch (err) {
        console.error(err)
      }
    }

    fetchDegrees()
  }, [user])

  const handlerCreateDegree = async () => {
    if (!degreeNameInput.trim() || !schoolInput.trim() || !creditInput.trim()) {
      alert('Todos los campos son obligatorios')
      return
    }

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/degrees/find-or-create/${user.id}`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            name: degreeNameInput,
            school: schoolInput,
            total_credits: Number(creditInput)
          })
        }
      )

      if (!res.ok) throw new Error('Error al crear o vincular la carrera')
      const degreeData = await res.json()

      setUserDegrees(prev => [...prev, degreeData])
      setDegreeNameInput('')
      setSchoolInput('')
      setCreditInput('')
    } catch (err) {
      console.error(err)
      alert('Error al crear o asociar la carrera')
    }
  }

  const handleDegreeClick = (degree) => {
    alert(`Carrera seleccionada: ${degree.name} (${degree.school}) - ${degree.total_credits} créditos`)
  }

  return (
    <>
      <div className="User">
        <h1>Carreras asociadas a {user.name}</h1>
        <div className="user-degrees">
          {userDegrees.map((d) => (
            <button
              key={d.id}
              className="degree-button"
              onClick={() => handleDegreeClick(d)}
            >
              {d.name} - {d.school} ({d.total_credits} créditos)
            </button>
          ))}
        </div>
      </div>

      <div className="form">
        <input
          type="text"
          placeholder="Nombre de la carrera"
          value={degreeNameInput}
          onChange={(e) => setDegreeNameInput(e.target.value)}
        />
      </div>

      <div className="form">
        <input
          type="text"
          placeholder="Escuela"
          value={schoolInput}
          onChange={(e) => setSchoolInput(e.target.value)}
        />
      </div>

      <div className="form">
        <input
          type="text"
          placeholder="Total de créditos"
          value={creditInput}
          onChange={(e) => setCreditInput(e.target.value)}
        />
      </div>

      <button onClick={handlerCreateDegree}>Crear carrera</button>
    </>
  )
}

export default User
