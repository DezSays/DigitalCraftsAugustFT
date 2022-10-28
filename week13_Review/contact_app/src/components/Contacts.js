
import React from "react";
import ContactItems from './ContactItems'

const Contacts = ({contacts, deleteContact}) =>{
    return (<>
    <div className="container">
        <div className="row">
            <div className="col-8 offset-2">
                <ul>
                    {contacts.map(contactObj => {
                        return <ContactItems key={contactObj.id} contact={contactObj} onDelete={deleteContact}/>
                    })}
                </ul>
            </div>
        </div>
    </div>
    
    
    </>)
}
export default Contacts

