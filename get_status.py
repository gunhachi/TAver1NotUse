import cognitive_face as CF
from global_variables import personGroupId

Key = 'fe11152b086c457c92eb23fc4dabcc48'
CF.Key.set(Key)

res = CF.person_group.get_status(personGroupId)
print res
