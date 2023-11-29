// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.0;

contract Client {
    
    struct CLIENT_DATA {
        string REF_CLIENT;
        string HASH_PROFILE;
        string PREVIOUS_HASH_PROFILE;
        bool SELLER;
        string TIME; 
    } 

    mapping (string => CLIENT_DATA) private CLIENT_REGISTRY;

    event New_Client_Registered(string refClient);
    event Client_profile_updated( string refClient);

    function add_client_ref(string memory _refClient, string memory _hashProfile, bool _seller, string memory _time) public returns (bool success) {
     //Conditions to check
     require(bytes(CLIENT_REGISTRY[_refClient].REF_CLIENT).length == 0 , "the client is already registered");

     
     // Add a new client
     CLIENT_DATA memory new_client_data = CLIENT_DATA(_refClient, _hashProfile, _hashProfile, _seller ,_time );
     CLIENT_REGISTRY[_refClient] = new_client_data; 

     // emittig an event for adding new client    
     emit New_Client_Registered(_refClient);       
     return  true; 
     }

    function update_client_profile(string memory _refClient, string memory _newHashProfile, string memory _time) public returns (bool success) {

     
     // Add a new client
     
     CLIENT_REGISTRY[_refClient].PREVIOUS_HASH_PROFILE = CLIENT_REGISTRY[_refClient].HASH_PROFILE; 
     CLIENT_REGISTRY[_refClient].HASH_PROFILE = _newHashProfile;
     CLIENT_REGISTRY[_refClient].TIME = _time;


     // emittig an event for updating a profile client    
     emit Client_profile_updated(_refClient);       
     return  true; 
     }  

    function get_client_ref(string memory _refClient) public view returns (
        string memory refClient,
        string memory hashProfile,
        string memory previousHashProfile,
        bool seller,
        string memory time) {
        return(
            CLIENT_REGISTRY[_refClient].REF_CLIENT,
            CLIENT_REGISTRY[_refClient].HASH_PROFILE,
            CLIENT_REGISTRY[_refClient].PREVIOUS_HASH_PROFILE,
            CLIENT_REGISTRY[_refClient].SELLER,
            CLIENT_REGISTRY[_refClient].TIME
            );
    }


}
