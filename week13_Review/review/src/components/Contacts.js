// * PROMPT * //
// Create a component that displays three controlled inputs for 'Name', 'Email', and 'Phone' inside of a form. When the form is submitted, create a new object including all the properties from the form. Add this object into an array in the state. When there is one or more item/s in the array, display the details for each item as a list of contacts with their contact info below each.


import React, {useState} from 'react'

const Contacts = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [list, setList] = useState([]);



  const handleSubmit = (e) => {
    e.preventDefault();
    let newContact = [name, email, phone, ...list]
    setList(newContact)
    setName("")
    setEmail("")
    setPhone("")
    

    console.log(list);
  }

    
  return (
    <>
      <h2>Contact List</h2>
      <br />

      <h3>Add new contact: </h3>

    
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder='Name' value={name} onChange={e=>setName(e.target.value)}/>
        <br />
        <input type="text" placeholder='Email' value={email} onChange={e=>setEmail(e.target.value)}/>
        <br />
        <input type="text" placeholder='Phone' value={phone} onChange={e=>setPhone(e.target.value)}/>
        <br />

        <button type="submit">Add Contact</button> 
      </form>


    <ul>
       {list.map(listItem =>{
           return <li key={listItem}>{listItem}</li>;
       })}
       
    </ul>

    </>
  )
}

export default Contacts