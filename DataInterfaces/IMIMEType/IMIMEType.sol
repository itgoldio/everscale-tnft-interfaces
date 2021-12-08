pragma ton-solidity = 0.47.0;

interface IMIMEType {

	function getMIMEType() external returns (string mimeType);
	function getMIMETypeResponsible() external responsible returns (string mimeType);

}

library MIMETypeLib {

	int constant ID = 7;

}

abstract contract MIMEType is IMIMEType {

    string _mimeType;

    function getMIMEType() external override returns (string mimeType) {
        return _mimeType;
    }

	function getMIMETypeResponsible() external override responsible returns (string mimeType) {
        return {value: 0, flag: 64}(_mimeType);
    }

}