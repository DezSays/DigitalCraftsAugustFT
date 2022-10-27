import React, {useState} from 'react'

const Forms = () => {

  const [count, setCount] = useState(0) // like saying let count = 0
  const [text, setText] = useState('howdy') // like saying let text = 'howdy'
  const [isValid, setIsValid] = useState(true) // this sets the checkbox to initially be unchecked
  return (
    <>
        <h2>{count}</h2>
        <h2>{text}</h2>
        <h3>{isValid ? "true" : "false"}</h3>

        <button onClick={() => setCount(count+1)}>click me!</button>
        <form>
          {/* how to set text value */}
          <input type='text' value={text} onChange={e => setText(e.target.value)} />
          <br />

          {/* how to set a checkbox */}
          <input type="checkbox" value={isValid} defaultChecked={isValid} onChange={(e) => setIsValid(e.target.checked)}/>
        </form>
    </>
  )
}

export default Forms