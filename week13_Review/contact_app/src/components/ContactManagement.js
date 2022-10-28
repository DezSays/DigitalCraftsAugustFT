import React, {useState, useEffect} from 'react'
import {v4 as uuidv4} from 'uuid'
import AddContact from './AddContact'
import Contacts from './Contacts'

const ContactManagement = () => {

  const [contacts, setContacts] = useState([]) 



  useEffect(() => {
    
    
    setContacts([
      {
        id: uuidv4(), 
        name: 'Dezarea Bryan',
        email: 'dezareabryan@gmail.com',
        phone: '706-301-6789',
        address: '13 Test Me Drive',
        city: 'Woodstock',
        state: 'GA',
        zip: '30189'
        
      },
      {
        id: uuidv4(), 
        name: 'Chewie',
        email: 'Chewie@gmail.com',
        phone: '706-222-2222',
        address: '156 LAla Rd',
        city: 'Houston',
        state: 'TX',
        zip: '45656'
        
      },
      {
        id: uuidv4(), 
        name: 'Gary',
        email: 'gary@gmail.com',
        phone: '706-111-2516',
        address: '888 Garys Place',
        city: 'Atlanta',
        state: 'GA',
        zip: '30133'
        
      }
      


    ])
  }, [])

  const handleAddContact = (newContact) => {
    setContacts([newContact, ...contacts])
  }

  const handleRemoveContact = (id) => {
    let filteredContact = contacts.filter(contact =>{

      return id !== contact.id;

    })

    setContacts(filteredContact)
  }

  

  return (
    <>
      <h1>Contact Management List</h1>

      <Contacts contacts={contacts} deleteContact={id =>handleRemoveContact(id)}/>

      <AddContact addContact={contact => handleAddContact(contact)}/>
    </>
  )
}

export default ContactManagement
