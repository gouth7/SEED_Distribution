from stellar_base.builder import Builder

with open('pk.txt') as data_file:
    data = data_file.read()
data = data.split()

collective_seed = #insert private key as string here
bad = []

for item in data:
    print("\n ------- sending 1000 SEED to {} -------".format(item))
    try:
        builder = Builder(secret=collective_seed, network='PUBLIC')
        builder.append_payment_op(item, '1000', 'SEED', 'GDPFSEBZO2W4TLWZO7FIMMG3QONHXYVF6LUULI6HUJS6PJLE4TRZEXLF')
        builder.sign()
        result = builder.submit()
        if 'status' in result:
            bad.append(item)
            print("Transaction failed. Status Code: {}. More info: {}.".format(result['status'], result['extras']['result_codes']))
    except Exception as e:
        print("could not send SEED to {} because: {}".format(item, e))
        bad.append(item)

print("Transaction did not work for the following public keys: {}".format(bad))

bad_file = open("failed_transactions.txt", 'w')
for item in bad:
    bad_file.write("{} \n".format(item))
bad_file.close()
