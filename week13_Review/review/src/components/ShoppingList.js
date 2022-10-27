import React, {useState} from 'react'

const ShoppingList = () => {


  const [text, setText] = useState('howdy') // like saying let text = 'howdy'



// Create HTML elements (helper function)
function makeElement() {
    return document.createElement('li')
}


  const handleSubmit = (e) => {
    e.preventDefault()

    let dataObj = {
      text
    }
    let res = dataObj.text
    let newEl = makeElement()
    document.body.append(newEl)
    newEl.append(res)


    
  }


  return (
    <>

        <h2>{text}</h2>



        <form onSubmit={handleSubmit}>
          {/* how to set text value */}
          <input type='text' value={text} onChange={e => setText(e.target.value)} />
          <br />

          <button type='submit'>submit</button>
        </form>
    </>
  )
}

export default ShoppingList