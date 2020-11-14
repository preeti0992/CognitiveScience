# Userdata = request.get_json(force=True)
# emotion_data = Userdata['emotions']

emotions = ['rage', 'anger', 'desperation', 'fear']
#probabilities_emotions = [0.53, 0.47, 0.34, 0.16]
#Probabilities of Emotion Patterns Seen 
prob_emo = [0.033, 0.1, 0.13, 0.067, 0.16, 0.267, 0.033, 0.1, 0.033, 0.067]
sit = ['psychological_issue', 'relationship_issue', 'addiction', 'trauma_abuse', 'frustration', 'jealousy',
 'under_influence', 'brutality', 'humiliation', 'financial', 'argument_fight', 'revenge_satisfaction']
prob_sit = [0.2, 0.43, 0.16, 0.3, 0.033, 0.2, 0.1, 0.13, 0.033, 0.1, 0.16, 0.13]

fear = ['fear']
anger = ['anger']
rage = ['rage']
desperation = ['desperation']
psychological_issue = ['psychological_issue']
relationship_issue = ['relationship_issue']
addiction = ['addiction']
trauma_abuse = ['trauma_abuse']
frustration = ['frustration']
jealousy = ['jealousy']
under_influence = ['under_influence']
brutality = ['brutality']
humiliation = ['humiliation']
financial = ['financial']
argument_fight = ['argument_fight']
revenge_satisfaction = ['revenge_satisfaction']

#emotion_data- emotion array received from UI 
#situation_data- situation array received from UI 

def check():
#    print('I am here.')
    return


def getProb( emotion_data, situation_data ):
#    print('I am here in get Prob.')
#    print('emotion_data',emotion_data)
#    print('situation_data',situation_data)
    if set(fear).intersection(emotion_data) and set(anger).intersection(emotion_data) and set(rage).intersection(emotion_data): 
        if set(trauma_abuse).intersection(situation_data) and set(jealousy).intersection(situation_data):
            probability = prob_emo[6] + prob_sit[3] + prob_sit[5]
            return probability
        else:
            probability = prob_emo[6]
            return probability
    
    if set(fear).intersection(emotion_data) and set(anger).intersection(emotion_data): 
        if set(psychological_issue).intersection(situation_data) and set(relationship_issue).intersection(situation_data): 
            probability = prob_emo[0] + prob_sit[0] + prob_sit[1]
            return probability
        else:
            probability = prob_emo[0]
            return probability

    if set(rage).intersection(emotion_data) and set(anger).intersection(emotion_data): 
        if set(relationship_issue).intersection(situation_data) and set(addiction).intersection(situation_data) and set(jealousy).intersection(situation_data) and set(brutality).intersection(situation_data):
           probability = prob_emo[1] + prob_sit[1] + prob_sit[5] + prob_sit[7]
           return probability
        if set(trauma_abuse).intersection(situation_data) and set(financial).intersection(situation_data):
           probability = prob_emo[1] + prob_sit[3] + prob_sit[9]
           return probability
        if set(addiction).intersection(situation_data) and set(revenge_satisfaction).intersection(situation_data):
            probability = prob_emo[1] + prob_sit[2] + prob_sit[11]
            return probability
        else:
            probability = prob_emo[1]
            return probability


    if set(anger).intersection(emotion_data) and set(desperation).intersection(emotion_data): 
        if set(psychological_issue).intersection(situation_data) and set(jealousy).intersection(situation_data) and set(revenge_satisfaction).intersection(situation_data):
            probability = prob_emo[2] + prob_sit[0] + prob_sit[5] + prob_sit[11]
            return probability
        if set(relationship_issue).intersection(situation_data) and set(revenge_satisfaction).intersection(situation_data):
            probability = prob_emo[2] + prob_sit[1] + prob_sit[11]
            return probability
        if set(trauma_abuse).intersection(situation_data) and set(financial).intersection(situation_data):
            probability = prob_emo[2] + prob_sit[3] + prob_sit[9]
            return probability
        if set(financial).intersection(situation_data): 
            probability = prob_emo[2] + prob_sit[9]
            return probability
        else: 
            probability = prob_emo[2]
            return probability


    if set(fear).intersection(emotion_data) and set(desperation).intersection(emotion_data): 
        if set(psychological_issue).intersection(situation_data):
            probability = prob_emo[3] + prob_sit[0]
            return probability
        if set(trauma_abuse).intersection(situation_data):
            probability = prob_emo[3] + prob_sit[9]
            return probability
        else: 
            probability = prob_emo[3]
            return probability


    if set(rage).intersection(emotion_data) and set(desperation).intersection(emotion_data): 
        if set(relationship_issue).intersection(situation_data) and set(under_influence).intersection(situation_data) and set(argument_fight).intersection(situation_data): 
            probability = prob_emo[7] + prob_sit[1] + prob_sit[6] + prob_sit[10]
            return probability
        if set(relationship_issue).intersection(situation_data) and set(brutality).intersection(situation_data): 
            probability = prob_emo[7] + prob_sit[1] + prob_sit[7]
            return probability
        else: 
            probability = prob_emo[7]
            return probability

    if set(fear).intersection(emotion_data) and set(rage).intersection(emotion_data): 
        if set(psychological_issue).intersection(situation_data) and set(addiction).intersection(situation_data) and set(trauma_abuse).intersection(situation_data) and set(under_influence).intersection(situation_data) and set(brutality).intersection(situation_data) and set(argument_fight).intersection(situation_data) and set(revenge_satisfaction).intersection(situation_data):
            probability = 0.99
            return probability
        else: 
            probability = prob_emo[8]
            return probability

    if set(desperation).intersection(emotion_data): 
        if set(relationship_issue).intersection(situation_data) and set(financial).intersection(situation_data):  
            probability = prob_emo[9] + prob_sit[1] + prob_sit[9]
            return probability
        if set(psychological_issue).intersection(situation_data): 
            probability = prob_emo[9] + prob_sit[0]
            return probability
        else:
            probability = prob_emo[9]
            return probability


    if set(anger).intersection(emotion_data): 
        if set(addiction).intersection(situation_data) and set(jealousy).intersection(situation_data):
            probability = prob_emo[4] + prob_sit[2] + prob_sit[5]
            return probability
        if set(relationship_issue).intersection(situation_data) and set(argument_fight).intersection(situation_data) and set(under_influence).intersection(situation_data):
            probability = prob_emo[4] + prob_emo[1] + prob_emo[10] + prob_emo[6]
            return probability
        if set(psychological_issue).intersection(situation_data) and set(humiliation).intersection(situation_data) and set(argument_fight).intersection(situation_data):
            probability = prob_emo[4] + prob_sit[0] + prob_sit[8] + prob_sit[10]
            return probability
        if set(relationship_issue).intersection(situation_data) and set(argument_fight).intersection(situation_data):
            probability = prob_emo[4] + prob_sit[1] + prob_sit[10]
            return probability
        if set(relationship_issue).intersection(situation_data): 
            probability = prob_emo[4] + prob_sit[1]
            return probability
        else: 
            probability = prob_emo[4]
            return probability

    if set(rage).intersection(emotion_data): 
        if set(trauma_abuse).intersection(situation_data) and set(jealousy).intersection(situation_data): 
            probability = prob_emo[5] + prob_sit[3] + prob_sit[5]
            return probability
        if set(relationship_issue).intersection(situation_data) and set(trauma_abuse).intersection(situation_data):
            probability = prob_emo[5] + prob_sit[1] + prob_sit[3]
            return probability
        if set(frustration).intersection(situation_data):
            probability = prob_emo[5] + prob_sit[4]
            return probability
        if set(relationship_issue).intersection(situation_data):
            probability = prob_emo[5] + prob_sit[1]
            return probability
        if set(addiction).intersection(situation_data): 
            probability = prob_emo[5] + prob_sit[2]
            return probability
        if set(trauma_abuse).intersection(situation_data): 
            probability = prob_emo[5] + prob_sit[3]
            return probability
        else: 
            probability = prob_emo[5]
            return probability

    else: 
        message = "The emotions and situation not in data! Chance of murder is minimal"
        return message
