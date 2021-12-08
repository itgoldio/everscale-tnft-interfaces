import tonos_ts4.ts4 as ts4

eq = ts4.eq

ts4.init('./', verbose = True)
VENDORING_PATH='../../../vendoring/'

#deploy
keypair = ts4.make_keypair()
setcodemultisig = ts4.BaseContract(VENDORING_PATH + 'setcodemultisig/SetcodeMultisigWallet', ctor_params = {'owners': [keypair[1]], 'reqConfirms': 1}, keypair = keypair)

codeIndex = ts4.load_code_cell(VENDORING_PATH + 'compiled/Index.tvc')
codeData = ts4.load_code_cell(VENDORING_PATH + 'compiled/Data.tvc')

# 73616d706c652e75726c (in hex) = sample.url
customInterfacesUrl = "73616d706c652e75726c"
nftRoot = ts4.BaseContract('compiled/NftRoot', ctor_params = {'codeIndex': codeIndex, 'codeData': codeData, 'ownerPubkey': keypair[1], 'customInterfacesUrl': customInterfacesUrl}, keypair = keypair)

ts4.dispatch_messages()

#id
IRequiredInterfaces = 1
ICustomInterfaces = 41000
ReqInterfaces = [IRequiredInterfaces, ICustomInterfaces]

answReqInterfaces = nftRoot.call_getter('getRequiredInterfaces')
answCustIntUrl = nftRoot.call_getter('getCustomInterfacesUrl')

assert eq(answCustIntUrl, customInterfacesUrl)
assert eq(answReqInterfaces, ReqInterfaces)