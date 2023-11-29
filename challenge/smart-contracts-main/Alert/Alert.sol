// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.0;

contract Contract {
    struct CLIENT_ALERT {
        string REF_CLIENT;
        int[] ALERT_TYPES;
        string COMMENT;
    }

    CLIENT_ALERT[] CLIENT_ALERT_REGISTRY; 

    function add_alert_message(string memory _refClient, int[] memory _alertTypes , string memory _comment) public returns (bool success) {

     CLIENT_ALERT memory new_alert = CLIENT_ALERT(_refClient, _alertTypes, _comment);   
     CLIENT_ALERT_REGISTRY.push(new_alert);
      
     return  true; 
     }

    function get_all_alerts() public view returns (CLIENT_ALERT[] memory all_alerts){
        return CLIENT_ALERT_REGISTRY;
    }

}
