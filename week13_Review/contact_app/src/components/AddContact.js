import React, {useState} from 'react'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button';
import {v4 as uuidv4} from 'uuid'


//   - name 
//   - e-mail 
//   - phone number 
//   - address 
//   - city 
//   - state 
//   - zip code


const AddContact = ({addContact}) => {


  
  const [name, setName] = useState("")
  const [email, setEmail] = useState("")
  const [phone, setPhone] = useState("")
  const [address, setAddress] = useState("")
  const [city, setCity] = useState("")
  const [state, setState] = useState("")
  const [zip, setZip] = useState("")

  const handleSubmit = (e) => {
    e.preventDefault()
    let newContact = {
      id: uuidv4,
      name,
      email,
      phone,
      address,
      city,
      state,
      zip
    }

    addContact(newContact) 
  }

  return (
    <>
      

      <div className="container">
        <div className="row">
          <div className="col-8 offset-2">

          <Form onSubmit={handleSubmit}>


            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Name</Form.Label>
              <Form.Control type="text" placeholder="Name" value={name} 
              onChange={e=> setName(e.target.value)}/>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Email</Form.Label>
              <Form.Control type="text" placeholder="Email" value={email} 
              onChange={e=> setEmail(e.target.value)}/>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Phone</Form.Label>
              <Form.Control type="text" placeholder="Phone" value={phone} 
              onChange={e=> setPhone(e.target.value)}/>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Address</Form.Label>
              <Form.Control type="text" placeholder="Address" value={address} 
              onChange={e=> setAddress(e.target.value)}/>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>City</Form.Label>
              <Form.Control type="text" placeholder="City" value={city} 
              onChange={e=> setCity(e.target.value)}/>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>State</Form.Label>
              <Form.Control type="text" placeholder="State" value={state} 
              onChange={e=> setState(e.target.value)}/>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Zip</Form.Label>
              <Form.Control type="text" placeholder="Zip" value={zip} 
              onChange={e=> setZip(e.target.value)}/>
            </Form.Group>
           
            <Button variant="primary" type="submit">
              Submit
            </Button>
          </Form>
            </div>
          </div>
      </div>
    </>
  )
}

export default AddContact
