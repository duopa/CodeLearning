pragma solidity ^0.4.0;

import “solidity_for_import.sol”

// This is a Contract

contract Test {
    uint a;

    function setA(uint x) public {
        a = x;
        emit Set_A(x);
    }

    event Set_A(uint a);

    struct Position{
        int lat;
        int lng;
    }

    address public ownerAddr;

    //函数修改器
    modifier owner () {
        require(msg.sender == owerAddr);
        _;
    }

    function mine() public owner {
        a +=1;
    }

}