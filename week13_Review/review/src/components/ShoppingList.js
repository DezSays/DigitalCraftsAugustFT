// Dez method

// import React, {useState} from 'react'

// const ShoppingList = () => {

//   const [text, setText] = useState('') 

// // Create HTML elements (helper function)
// function makeElement() {
//     return document.createElement('li')
// }

//   const handleSubmit = (e) => {
//     e.preventDefault()

//     let dataObj = {
//       text
//     }

//     let res = dataObj.text
//     let newEl = makeElement()
//     document.body.append(newEl)
//     newEl.append(res)   

//   }
//   return (
//     <>
//         <h2>{text}</h2>
//         <form onSubmit={handleSubmit}>
//           <input type='text' value={text} onChange={e => setText(e.target.value)} />

//           <br />

//           <button type='submit'>submit</button>
//         </form>
//     </>
//   )
// }

// export default ShoppingList


// Veronica's Method

import React, {useState} from 'react'

const ShoppingList = () => {
  const [item, setItem] = useState("");
  const [list, setList] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    let newList = [item, ...list]
    setList(newList)
    setItem("")

    console.log(list);
  }
    
  return (
    <>
      <h2>Shopping List</h2>
      <br />

      <h3>Add new Item:</h3>

    
      <form onSubmit={handleSubmit}>
        <input type="text" value={item} onChange={e=>setItem(e.target.value)}/>
        <br />

        <input type="submit" />
      </form>


    <ul>

       {list.forEach(listItem =>{
           return <li key={listItem}>{listItem}</li>
       })}
    </ul>

    </>
  )
}

export default ShoppingList


