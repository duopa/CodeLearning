pragma solidity ^0.4.0;

import "solidity_for_import.sol";

// This is a Contract

contract Test {
    uint a;
    bool boola = true;
    bool boolb = false;
    int256 b = 20;
    int256 c = 30;

    function testadd() public returns (int) {
        if (b>c) {
            return b+c;
        } else if (b==c){
            return b * c;
        } else{
            return b >> 2;
        }
    }

    function testbool() public returns (bool) {
        return !boola;
    }

    function testbool() public returns (bool) {
        return boola || boolb
    }

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