import { useState, useEffect } from 'react'

function Degree({ user, degree }) {
  const [degreeCourses, setDegreeCourses] = useState([]) 

  useEffect(() => {
    if (!user || !degree) return

    const fetchCourses = async ( ) => {
      try {

      } catch (err) {
        
      }
    }
  })

  return (
    <>
      <div className='Degree'>
        <h1>Vista de la carrera</h1>
      </div>
    </>
  )
}

export default Degree