// SPDX-License-Identifier: MIT 
pragma solidity ^0.6.0;


contract SimpleStorage  {
    //gets initialized as zero  
    uint256 favoriteNumber;
    
    struct People {
        uint256 favoriteNumber;
        string  name;
    }

    People [] public people;
    mapping(string => uint256)public nameToFavoriteNumber;
 
    function store (uint256 _favoriteNumber)public{
    favoriteNumber = _favoriteNumber; 
    }

    function addPerson(string memory _name,uint256 _favoriteNumber)public {
    people.push(People(_favoriteNumber ,_name));
    nameToFavoriteNumber[_name]=_favoriteNumber;
    }
   function retrieve()public pure  returns  {
   
    return favoriteNumber;
    }
}