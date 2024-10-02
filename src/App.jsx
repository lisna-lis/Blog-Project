

import './App.css'
import Avatar from './components/Avatar'
import Cards from './components/Cards'

import Navigation from './components/Navigation'
import Postcard from './components/Postcard'
import Postformcard from './components/Postformcard'


function App() {


  return (
    
     <div className='flex mt-4 max-w-4xl mx-auto gap-6 '>
      <div className='w-4/12'>
      
      <Navigation/>
      
      </div>
      <div className='w-4/8'>
        <Postformcard></Postformcard>
         
       <Postcard></Postcard>
        </div>
     </div>
    
  )
}

export default App
