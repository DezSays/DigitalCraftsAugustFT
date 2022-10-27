import React, {useState} from 'react'

const App = () => {
  const [count, setCount] = useState(0)
  const handleClick = () =>{
    console.log('button clicked')
  }
  return (
    <>
    <h1>{count}</h1>
    <button onClick={handleClick}>console log button click</button>
    <button onClick={()=>setCount(count+1)}>update UI</button>
    </>
  )
}

export default App

// const wrapper = () => {
//   return setCount(count+1)
// }
// Above is an explicit return, see that the return keyword is used

// Below is an implicit function
const wrapper = () => setCount(count+1)