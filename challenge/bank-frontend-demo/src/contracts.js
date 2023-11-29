
import {ethers} from "ethers";

const SC_CLIENT = '0x5b591CB6f5ABf3b209bd1D3cEcA698bbF4BA9728'; 
const SC_AML = '0x202823049F6Fd0C0Fb8E9878Cb219525b20D75E4'; 



export async function storeNewClient(refClient, hashProfile, seller, time) {
    const provider = new ethers.BrowserProvider(window.ethereum)
    const signer = await provider.getSigner();
    let abi = JSON.parse(`[ { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "string", "name": "refClient", "type": "string" } ], "name": "Client_profile_updated", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "string", "name": "refClient", "type": "string" } ], "name": "New_Client_Registered", "type": "event" }, { "inputs": [ { "internalType": "string", "name": "_refClient", "type": "string" }, { "internalType": "string", "name": "_hashProfile", "type": "string" }, { "internalType": "bool", "name": "_seller", "type": "bool" }, { "internalType": "string", "name": "_time", "type": "string" } ], "name": "add_client_ref", "outputs": [ { "internalType": "bool", "name": "success", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_refClient", "type": "string" } ], "name": "get_client_ref", "outputs": [ { "internalType": "string", "name": "refClient", "type": "string" }, { "internalType": "string", "name": "hashProfile", "type": "string" }, { "internalType": "string", "name": "previousHashProfile", "type": "string" }, { "internalType": "bool", "name": "seller", "type": "bool" }, { "internalType": "string", "name": "time", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_refClient", "type": "string" }, { "internalType": "string", "name": "_newHashProfile", "type": "string" }, { "internalType": "string", "name": "_time", "type": "string" } ], "name": "update_client_profile", "outputs": [ { "internalType": "bool", "name": "success", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" } ]`);
    const contract = new ethers.Contract(SC_CLIENT, abi, signer);
    const result = await contract.add_client_ref(refClient, hashProfile, seller, time).then();
    console.log("test block",await result.wait().then());

    // it will return the hash of the transaction as proof of success

    return result.hash

}

export async function updateClient(refClient, hashProfile, time) {
    const provider = new ethers.BrowserProvider(window.ethereum)
    const signer = await provider.getSigner();
    let abi = JSON.parse(`[ { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "string", "name": "refClient", "type": "string" } ], "name": "Client_profile_updated", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "string", "name": "refClient", "type": "string" } ], "name": "New_Client_Registered", "type": "event" }, { "inputs": [ { "internalType": "string", "name": "_refClient", "type": "string" }, { "internalType": "string", "name": "_hashProfile", "type": "string" }, { "internalType": "bool", "name": "_seller", "type": "bool" }, { "internalType": "string", "name": "_time", "type": "string" } ], "name": "add_client_ref", "outputs": [ { "internalType": "bool", "name": "success", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_refClient", "type": "string" } ], "name": "get_client_ref", "outputs": [ { "internalType": "string", "name": "refClient", "type": "string" }, { "internalType": "string", "name": "hashProfile", "type": "string" }, { "internalType": "string", "name": "previousHashProfile", "type": "string" }, { "internalType": "bool", "name": "seller", "type": "bool" }, { "internalType": "string", "name": "time", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_refClient", "type": "string" }, { "internalType": "string", "name": "_newHashProfile", "type": "string" }, { "internalType": "string", "name": "_time", "type": "string" } ], "name": "update_client_profile", "outputs": [ { "internalType": "bool", "name": "success", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" } ]`);
    const contract = new ethers.Contract(SC_CLIENT, abi, signer);
    const result = await contract.update_client_profile(refClient, hashProfile, time).then();
    console.log(await result.wait().then());

    // it will return the hash of the transaction as proof of success

    return result.hash; 
}

export async function getClient(refClient) {
    const provider = new ethers.BrowserProvider(window.ethereum)
    const signer = await provider.getSigner();
    let abi = JSON.parse(`[ { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "string", "name": "refClient", "type": "string" } ], "name": "Client_profile_updated", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "string", "name": "refClient", "type": "string" } ], "name": "New_Client_Registered", "type": "event" }, { "inputs": [ { "internalType": "string", "name": "_refClient", "type": "string" }, { "internalType": "string", "name": "_hashProfile", "type": "string" }, { "internalType": "bool", "name": "_seller", "type": "bool" }, { "internalType": "string", "name": "_time", "type": "string" } ], "name": "add_client_ref", "outputs": [ { "internalType": "bool", "name": "success", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_refClient", "type": "string" } ], "name": "get_client_ref", "outputs": [ { "internalType": "string", "name": "refClient", "type": "string" }, { "internalType": "string", "name": "hashProfile", "type": "string" }, { "internalType": "string", "name": "previousHashProfile", "type": "string" }, { "internalType": "bool", "name": "seller", "type": "bool" }, { "internalType": "string", "name": "time", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_refClient", "type": "string" }, { "internalType": "string", "name": "_newHashProfile", "type": "string" }, { "internalType": "string", "name": "_time", "type": "string" } ], "name": "update_client_profile", "outputs": [ { "internalType": "bool", "name": "success", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" } ]`);
    const contract = new ethers.Contract(SC_CLIENT, abi, signer);
    const result = await contract.get_client_ref(refClient).then();
    console.log(await result);

    // it will return an array of string like this 
    //[ "refClient2", "RSSOFKvkAsHBPKKmK+q0zQ==", "N4aIlAWyFm+ghPLJeMGiNA==", true, "11/29/2023, 11:07:30 AM"
    // 0  : ref client , 1 : hash, 2: previous hash , 3 : boolen if it is a seller or not , 4 : date 

    return result; 
}


export async function check_rule2(refClient, transactionVolume) {
    const provider = new ethers.BrowserProvider(window.ethereum)
    const signer = await provider.getSigner();
    let abi = JSON.parse(`[{"inputs":[{"internalType":"string","name":"_refClient","type":"string"},{"internalType":"int256","name":"_largeTransactionVolume","type":"int256"}],"name":"check_aml_rule2","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_refClient","type":"string"},{"internalType":"int256","name":"_receiverNumber","type":"int256"}],"name":"check_aml_rule7","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_refClient","type":"string"}],"name":"get_aml_status","outputs":[{"internalType":"string","name":"refClient","type":"string"},{"internalType":"int256","name":"rule2_status","type":"int256"},{"internalType":"int256","name":"rule7_status","type":"int256"}],"stateMutability":"view","type":"function"}]`);
    const contract = new ethers.Contract(SC_AML, abi, signer);
    const result = await contract.check_aml_rule2(refClient, transactionVolume).then();
    console.log(await result.wait().then());

    // it will return the hash of the transaction as proof of success

    return result.hash; 
}

export async function check_rule7(refClient, receiverNumber) {
    const provider = new ethers.BrowserProvider(window.ethereum)
    const signer = await provider.getSigner();
    let abi = JSON.parse(`[{"inputs":[{"internalType":"string","name":"_refClient","type":"string"},{"internalType":"int256","name":"_largeTransactionVolume","type":"int256"}],"name":"check_aml_rule2","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_refClient","type":"string"},{"internalType":"int256","name":"_receiverNumber","type":"int256"}],"name":"check_aml_rule7","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_refClient","type":"string"}],"name":"get_aml_status","outputs":[{"internalType":"string","name":"refClient","type":"string"},{"internalType":"int256","name":"rule2_status","type":"int256"},{"internalType":"int256","name":"rule7_status","type":"int256"}],"stateMutability":"view","type":"function"}]`);
    const contract = new ethers.Contract(SC_AML, abi, signer);
    const result = await contract.check_aml_rule7(refClient, receiverNumber).then();
    console.log(await result.wait().then());

    // it will return the hash of the transaction as proof of success

    return result.hash; 
}


export async function get_aml_status(refClient) {
    const provider = new ethers.BrowserProvider(window.ethereum)
    const signer = await provider.getSigner();
    let abi = JSON.parse(`[{"inputs":[{"internalType":"string","name":"_refClient","type":"string"},{"internalType":"int256","name":"_largeTransactionVolume","type":"int256"}],"name":"check_aml_rule2","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_refClient","type":"string"},{"internalType":"int256","name":"_receiverNumber","type":"int256"}],"name":"check_aml_rule7","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_refClient","type":"string"}],"name":"get_aml_status","outputs":[{"internalType":"string","name":"refClient","type":"string"},{"internalType":"int256","name":"rule2_status","type":"int256"},{"internalType":"int256","name":"rule7_status","type":"int256"}],"stateMutability":"view","type":"function"}]`);
    const contract = new ethers.Contract(SC_AML, abi, signer);
    const result = await contract.get_aml_status(refClient).then();

    const rule2_status = result['rule2_status'];
    const rule7_status = result['rule7_status'];

    // it returns 0 if the client is compliant with the rule , and 1 if he is not 
     
    let aml_status = {rule7_status, rule2_status}
    return aml_status; 
}