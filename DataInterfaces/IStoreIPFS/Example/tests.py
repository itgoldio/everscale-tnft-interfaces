import tonos_ts4.ts4 as ts4

eq = ts4.eq

ts4.init('./', verbose = True)
VENDORING_PATH='../../../vendoring/'

#deploy
keypair = ts4.make_keypair()
setcodemultisig = ts4.BaseContract(VENDORING_PATH + 'setcodemultisig/SetcodeMultisigWallet', ctor_params = {'owners': [keypair[1]], 'reqConfirms': 1}, keypair = keypair)

codeIndex = ts4.load_code_cell(VENDORING_PATH + 'compiled/Index.tvc')
codeData = ts4.load_code_cell('compiled/Data.tvc')

nftRoot = ts4.BaseContract('compiled/NftRoot', ctor_params = {'codeIndex': codeIndex, 'codeData': codeData}, keypair = keypair)

#send mint transaction
#68747470733a2f2f73616d706c652e636f6d2f (in hex) = https://sample.com/
dataUrl = "68747470733a2f2f73616d706c652e636f6d2f"
payload = ts4.encode_message_body('compiled/NftRoot', 'mintNft', {'dataUrl': dataUrl})
setcodemultisig.call_method_signed('sendTransaction', {'dest': nftRoot.address, 'value': 2000000000, 'bounce': False, 'flags': 0, 'payload': payload}, expect_ec = 0)
ts4.dispatch_messages()

#resolve data addr
addrData = nftRoot.call_getter('resolveData', {'addrRoot': nftRoot.address, 'id': 0})
ts4.Address.ensure_address(addrData)
data = ts4.BaseContract('compiled/Data', ctor_params = None, address = addrData)

#id
IRequiredInterfaces = 1
IStoreIPFS = 6
ReqInterfaces = [IRequiredInterfaces, IStoreIPFS]

answUrl = data.call_getter('getDataUrl')
answReqInterfaces = data.call_getter('getRequiredInterfaces')

assert eq(answUrl, bytes.fromhex(dataUrl).decode('utf-8'))
assert eq(answReqInterfaces, ReqInterfaces)