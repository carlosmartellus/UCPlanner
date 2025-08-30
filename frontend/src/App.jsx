import { useState } from 'react'
import './App.css'
import Home from './views/home/Home'
import User from './views/user/User'
import Degree from './views/degree/Degree'

function App() {
  const [appView, setAppView] = useState('home')
  const [user, setUser] = useState(null)
  const [degreeNameInput, setDegreeNameInput] = useState('')
  const [schoolInput, setSchoolInput] = useState('')
  const [creditInput, setCreditInput] = useState('')
  const [degree, setDegree] = useState(null) 

  return (
    <div className="App">
      {appView === 'home' && (
        <Home 
          user={user}
          setUser={setUser}
          setAppView={setAppView}
        />
      )}

      {appView === 'user' && (
        <User
          user={user}
          degreeNameInput={degreeNameInput}
          setDegreeNameInput={setDegreeNameInput}
          schoolInput={schoolInput}
          setSchoolInput={setSchoolInput}
          creditInput={creditInput}
          setCreditInput={setCreditInput}
          setAppView={setAppView}
          setDegree={setDegree}
        />
      )}

      {appView === 'degree' &&(
        <Degree
          user={user}
          degree={degree}
        />
      ) }
    </div>
  )
}

export default App
