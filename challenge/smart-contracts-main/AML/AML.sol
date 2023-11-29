// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.0;

// interface of Client contract 
contract Client {
    
    struct CLIENT_DATA {
        string REF_CLIENT;
        string HASH_PROFILE;
        string PREVIOUS_HASH_PROFILE;
        bool SELLER;
        string time; 
    } 

    mapping (string => CLIENT_DATA) private CLIENT_REGISTRY;

    event New_Client_Registered(string refClient);
    event Client_profile_updated( string refClient);

    function add_client_ref(string memory _refClient, string memory _hashProfile, string memory time) public returns (bool success) {     }

    function update_client_profile(string memory _refClient, string memory _newHashProfile, string memory _time) public returns (bool success) {}  

    function get_client_ref(string memory _refClient) public view returns ( string memory refClient, string memory hashProfile, string memory previousHashProfile,bool seller ,string memory time) {}

}


contract AML {

    struct AML_TRANSACTION_STATUS{ 
        string REF_CLIENT;
        int rule2_status;
        int rule7_status;
    }

    mapping (string => AML_TRANSACTION_STATUS) AML_TRANSACTIONS_REGISTRY;

    int buyerNumberThreshold = 15;

    
    // smart contract application
    Client client_sc = Client(0x5b591CB6f5ABf3b209bd1D3cEcA698bbF4BA9728);

    function check_rule2 (string memory _refClient, int _largeTransactionVolume) private returns (bool success){
        (, string memory _now , string memory _prev, , ) = client_sc.get_client_ref(_refClient);
        
        if ((_largeTransactionVolume > 1000) && (keccak256(abi.encodePacked(_prev)) != keccak256(abi.encodePacked(_now))) ) 
        {AML_TRANSACTIONS_REGISTRY[_refClient].rule2_status = 1;}
        return true; 
    }

    function check_rule7 (string memory _refClient, int _receiverNumber) private returns ( bool success){
        if (_receiverNumber < buyerNumberThreshold)   
        {AML_TRANSACTIONS_REGISTRY[_refClient].rule7_status = 1;}

        return true;
    }

    function check_aml_rule2(string memory _refClient, int _largeTransactionVolume) public returns (bool success){
        AML_TRANSACTIONS_REGISTRY[_refClient].REF_CLIENT= _refClient;
        check_rule2(_refClient, _largeTransactionVolume);
        return true;
    }

    function check_aml_rule7(string memory _refClient, int _receiverNumber) public returns (bool success){
        AML_TRANSACTIONS_REGISTRY[_refClient].REF_CLIENT= _refClient;
        (,,,bool seller,)=client_sc.get_client_ref(_refClient);
        if (seller){check_rule7(_refClient, _receiverNumber);}
        check_rule7(_refClient, _receiverNumber);
        return true;
    }

    
    function get_aml_status(string memory _refClient) public view returns (
        string memory refClient,
        int rule2_status,
        int rule7_status) {
        return(
            AML_TRANSACTIONS_REGISTRY[_refClient].REF_CLIENT,
            AML_TRANSACTIONS_REGISTRY[_refClient].rule2_status,
            AML_TRANSACTIONS_REGISTRY[_refClient].rule7_status
            );
    }

}

