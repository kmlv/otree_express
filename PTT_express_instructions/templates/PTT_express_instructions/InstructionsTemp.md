{# Greetings - ALL #}

* Welcome to the LEEPS Laboratory. During the course of this session, you will be asked to make a series of decisions. By participating in this study, you will earn real money that will be paid to you in cash at the end of the experiment. On top of what you will earn during the session, you will receive a participation fee of ${{ participation_fee }}. 

* It is important you do not speak out loud or talk to other participants during the duration of the session. If you have any question, please raise your hand and an experimenter will attend to your station. 

* This session has two stages. In Stage 1, called <em>Task Income Stage</em>, you will work on a set tasks to earn some money. We will refer to this amount as the <em>task income</em>. Specific instructions will be provided once this stage starts.

{#  Stage 2: general | All but TP #}
{% if treatment != 'TP' %}

* In Stage 2, called <em>Interaction Stage</em>, you will interact with another participant in the room. First, you will be anonymously paired with another participant. You will be randomly assigned to be either role <strong>A</strong> or role <strong>B</strong>. You will remain in the same role throughout the entire duration of the experiment, and will be informed about your role on your computer screen once Stage 2 starts. You will not be informed about the identity of the person you are paired with, neither during nor after the experiment. </p> </br>

* Role A: If you are role A, you are to decide how much of B’s <em>task income</em> you would like to transfer into your own account. You are able to transfer anywhere from 0 to 100 percent of B’s <em>task income</em>, but you will not be able to transfer B’s endowment. You will be making your decision on a screen like this one: </p> </br>

    <div style="align-content: center; border:1px solid lightgrey">
        <img src="{% static "PTT_express_instructions/A_decision_screen.png" %}"/>
    </div> </br>

* Role B: If you are role B, you will be asked to guess what percentage of your <em>task income</em> A transferred to his/her own account.</p>

{% endif %}



{#    Stage 2: general | only TP #}
{% if treatment  == 'TP' or role == 'TP-R' %}

* In Stage 2, there are three possible roles for each participant, role <em>A</em>, role <em>B</em> and the role <em>R</em>. First, One participant will be randomly selected to have the role R. The rest of participants will be anonymously paired in groups of two. Within each group, roles will be randomly assigned so that there will be one person with role A and one with role B. You will remain in the same role throughout the entire duration of the experiment, and will be informed about your role on your computer screen once Stage 2 starts. You will not be informed about the identity of the person you are paired with, neither during nor after the experiment.

* Role R: If you have role R, your only task is to <em>read</em> the messages written by players with role B who are able to send a message for the reader. The reader is the only participant that is going to read the messages. None of the other participants in today's session will ever read these messages. The reader will not receive any information about player A or B, but the messages players with role B. The reader will need to read and confirm receipt to each message from B participants. Not all players B will write a message or be able to send it, as it will be explained below.</p>

* Role A: 
* If you are role A, you are to decide how much of B’s <em>task income</em> you would like to transfer into your own account. You are able to transfer anywhere from 0 to 100 percent of B’s <em>task income</em>, but you will not be able to transfer B’s endowment. You will be making your decision on a screen like this one: </p> </br>

    <div style="align-content: center; border:1px solid lightgrey">
        <img src="{% static "PTT_express_instructions/A_decision_screen.png" %}"/>
    </div> </br>

* Role B: 
* If you are role B, you will be asked to guess what percentage of your <em>task income</em> A transferred to his/her own account.</p>
  {# Role B must continue in #}

{% endif %}


{#  No message end #}
{% if treatment == 'NM' %}
    {#  Nothing for now #}


{#  Free message end #}
{% if treatment == 'FM' %}

* After player A has taken a share of your task income, you will get the opportunity to write and send a message to player A.


{# Stage 2: paid messages DM/TP WTA/WTP BDMCONT/BDMLIST/SOP #}

{# paid messages: DM/TP WTA/WTP BDMCONT #}

{% if (treatment == 'DM' or treatment == 'TP') and  
value_type == 'WTP' and  
elicitation_method =='BDM' & BDM_type == 'CONT' %}

* After A has taken a share of your task income, you will have the opportunity to write a message for {% if treatment == 'DM' %} your counterpart, player A. {% elif treatment == 'TP' %} player R, the reader.{% endif %} 

* Then, you will be asked to state the maximum amount that you are willing to pay to send your message. We will refer to this amount as your valuation. 

* After you submit your valuation, you will learn the actual price of sending your message. This price is randomly generated by the computer and all numbers between $0 and {{ BDM_up_limit }} are equally likely. Your price will be drawn independently from prices drawn for other pairs.

* If your valuation is greater than or equal to the computer’s generated price, then your message will be sent, and you will pay the actual price generated by the computer. If your valuation is lower than the actual price, then you do not get to send your message.

{% elif (treatment == 'DM' or treatment == 'TP') and  
value_type == 'WTA' and  
elicitation_method =='BDM' & BDM_type == 'CONT' %}

* After A has taken a share of your task income, you will have the opportunity to write a message for {% if treatment == 'DM' %} your counterpart, player A. {% elif treatment == 'TP' %} player R, the reader.{% endif %}

* Then, you will be asked to state the minimum amount you would be willing to accept to forgo sending the message you wrote. We will refer to this amount as your valuation. 
                    
* After you submit your valuation, you will learn the actual compensation for not sending your message. The actual compensation is randomly generated by the computer and all numbers between $0 and {{ BDM_up_limit }} are equally likely. Your compensation will be drawn independently from compensations drawn for other pairs.

* If your valuation is smaller than the actual compensation, then your message will not be sent and you will receive the actual compensation. If your valuation is greater than or equal to the actual compensation, then your message will be delivered and you will not receive any compensation. 

{% endif %}







{# paid messages: DM/TP WTA/WTP BDMCONT #}

{% if (treatment == 'DM' or treatment == 'TP') and  
value_type == 'WTP' and  
elicitation_method =='BDM' & BDM_type == 'LIST' %}

* After A has taken a share of your task income, you will have the opportunity to write a message for {% if treatment == 'DM' %} your counterpart, player A. {% elif treatment == 'TP' %} player R, the reader.{% endif %} 

* Then, you will be asked whether you are willing to pay certain price to send your message or not. This question will be repeated for a number of different prices.  

* After you submit your responses, the computer will randomly select one of these prices. If you responded that you were willing to pay such price to send your message, then your message will be sent, and you will pay that price.  If you responded that you were not willing to pay such price to send your message, then your message will not be sent, and you will not pay anything. 

{% elif (treatment == 'DM' or treatment == 'TP') and  
value_type == 'WTA' and  
elicitation_method =='BDM' & BDM_type == 'LIST' %}

* After A has taken a share of your task income, you will have the opportunity to write a message for {% if treatment == 'DM' %} your counterpart, player A. {% elif treatment == 'TP' %} player R, the reader.{% endif %} 

* Then, you will be asked whether you are willing to accept certain amount to forgo sending the message you wrote; that is, in exchange for not sending the message. This question will be repeated for a number of different amounts of compensation.  

* After you submit your responses, the computer will randomly select one of these listed amounts. If you responded that you were willing to accept such amount in exchange for not sending your message, then your message will not be sent, and you will receive that amount. If you responded that you were not willing to accept  such amount for not sending your message, then your message will be sent, and you will not receive anything. 

{% endif %}



{# paid messages: DM/TP WTA/WTP BDMCONT #}

{% if (treatment == 'DM' or treatment == 'TP') and  
value_type == 'WTP' and  
elicitation_method =='SOP' %}

* After A has taken a share of your task income, you will have the opportunity to write a message for {% if treatment == 'DM' %} your counterpart, player A. {% elif treatment == 'TP' %} player R, the reader.{% endif %} 

* Then, you will be asked whether you are willing to pay certain price to send your message or not. If you respond positively, your message will be sent, and you will pay that price.  If you respond negatively, your message will not be sent, and you will not pay anything. 

{% elif (treatment == 'DM' or treatment == 'TP') and  
value_type == 'WTA' and  
elicitation_method =='SOP' %}

* After A has taken a share of your task income, you will have the opportunity to write a message for {% if treatment == 'DM' %} your counterpart, player A. {% elif treatment == 'TP' %} player R, the reader.{% endif %} 

* Then, you will be asked whether you are willing to accept certain amount to forgo sending the message you wrote; that is, in exchange for not sending the message. If you respond positively, your message will not be sent, and you will receive that amount. If you respond negatively, your message will be sent, and you will not receive any compensation.   


{% endif %}


{# everyone closing  #}

* After this interaction, both members of each pair will see the corresponding payoffs information. Also before the search tasks and after the interaction, you will be asked to answer a series of brief questions.




















































