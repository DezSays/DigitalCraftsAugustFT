import React, {useState} from 'react'

const Forms = () => {

  const [count, setCount] = useState(0) // like saying let count = 0
  const [text, setText] = useState('howdy') // like saying let text = 'howdy'
  const [isValid, setIsValid] = useState(true) // this sets the checkbox to initially be unchecked/checked
  const [city, setCity] = useState("SanFrancisco")

  // any function you create needs to be above the return function
  const handleSubmit = (e) => {
    e.preventDefault()

    // typically you want to pass this information in your api call as an object, one whole chunk, instead of piece by piece

    let dataObj = {
      text,
      isValid,
      city
    }
    console.log(dataObj)
  }
  return (
    <>
        <h2>{count}</h2>
        <h2>{text}</h2>
        <h3>{isValid ? "true" : "false"}</h3>
        <h3>{city}</h3>

        <button onClick={() => setCount(count+1)}>click me!</button>
        <form onSubmit={handleSubmit}>
          {/* how to set text value */}
          <input type='text' value={text} onChange={e => setText(e.target.value)} />
          <br />

          {/* how to set a checkbox */}
          <input type="checkbox" value={isValid} defaultChecked={isValid} onChange={(e) => setIsValid(e.target.checked)}/>
          <br />
          <select value={city} onChange={e=>setCity(e.target.value)}>
            <option value="Houston">Houston</option>
            <option value="Atlanta">Atlanta</option>
            <option value="Seattle">Seattle</option>
            <option value="Chicago">Chicago</option>
            <option value="NewYork">New York</option>
            <option value="SanFrancisco">San Francisco</option>
          </select>
          <button type='submit'>submit</button>
        </form>
    </>
  )
}

export default Forms