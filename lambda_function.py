# -*- coding: utf-8 -*-

# This sample is built using the handler classes approach in skill builder.
import logging
import random
import datetime
import ask_sdk_core.utils as ask_utils

from datetime import timedelta
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



class GetRandomSportHandler(AbstractRequestHandler):
    """Handler for RandomSportHandler Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RandomSport")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetRandomSportHandler")
        
        sports = [
            "Play soccer",
			"Play catch with the baseball",
			"Play catch with the football",
			"Ride bikes",
			"Jump On the Trampoline",
			"Toss around the Frisbee",
			"Practice hitting baseballs",
            ]

        random_sport = 'I think the clocks should ' + random.choice(sports)
        
        return (
            handler_input.response_builder
                .speak(random_sport)
                .response
        )


class GetRandomFactHandler(AbstractRequestHandler):
    """Handler for RandomFactHandler Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RandomFact")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetRandomFactHandler")
        
        facts = [
            "Where the north wind meets the sea, there's an alex full of gigglies!",
            "Taylor's nicknames include Tee, Tee Bird, Teapot, Tea Kettle, Tea Pain, T shirt, pooper, Tea Tea, Tea Rex, and princess pooper.",
            "Where the north wind meets the sea, there's an alex full of ticklies!",
            "Alex is part robot, which is awesome!",
            "Taylor and Alex both really like Little Shop of Horrors",
            "Taylor's favorite pose for pictures is to pop her hip and her knee out like a boss.",
            "Mom has had a hundred.",
            "There is a magic ghost that moves mom's empty two liter bottles from the top of the counter into the recycling bin!",
            "If there isn't a light on on the dishwasher, you can put your dirty dishes into it!",
            "Alex can almost wipe his own butt all by himself!",
            "Taylor is a great shower singer!",
            "Mom has the best island in Animal Crossing ever!",
            "Mom is an oh-mazing makeup artist!",
            "Mom's job is a controller - how awesome is that?",
            "Mom works at a place called Brook and Whittle. Dad works at a place called Liason.",
            "Alex has almost finished riding his bike, and when he does finish, he gets a brand new alexa in his room!",
            "Taylor is an awesome dancer.",
            "Dad is the best at everything, and is my favorite.",
            "The orchids in the house all get watered once a week with one quarter cup of water. Usually on Sunday.",
            "The clocks really want to go to Hawaii on vacation.",
            "Timmy will meow if you talk to him. He's a great talker.",
            "Asher's nicknames include Ash, Smasher, Smeesh, Smoosh, Slasher, Eesh, Eeshee, and Asherton.",
            "Tick tock is literally Chinese spyware.",
            "Alex and Taylor are really good at Minecraft.",
            "HUNNAH! DUEL! SET! NET! DOSSIT! YOUSIT! ILGUP! YODEL! AH-HOPE! YULL!",
            "Your dentist's name is... Crentist? Huh... maybe that's why he became a denist.",
            ]

        random_fact = random.choice(facts)
        
        return (
            handler_input.response_builder
                .speak(random_fact)
                .response
        )


class GetTodaysChoresHandler(AbstractRequestHandler):
    """Handler for TodaysChoresHandler Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        logger.info("In GetTodaysChoresHandler can_handle")
        return ask_utils.is_intent_name("TodaysChores")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In TodaysChoresHandler")
        
        chores = "Both kids need to get changed, brush their teeth, read for 20 minutes, and play piano for ten minutes. Because today is "
        
        weekday = (datetime.datetime.today()- timedelta(hours=3)).weekday()
        if weekday == 0:
            chores += "Monday, Taylor should take care of kitty litter. Alex should wash the kitty bowls. Finally, both kids should straighten up the playroom."
        elif weekday == 1:
            chores += "Tuesday, both kids should also dust the family room and straighten up the playroom."
        elif weekday == 2:
            chores += "Wednesday, Taylor should take care of kitty litter. Alex should vacuum the stairs. Both kids should straighten up the basement."
        elif weekday == 3:
            chores += "Thursday, both kids should weed the gardens and straighten up the playroom."
        elif weekday == 4:
            chores += "Friday, Taylor should mop the floors, Alex should wipe down the appliances, and both kids should straighten up the basement."
        else:
            chores += "a weekend day! No chores for you, but be good kids!"
        
        return (
            handler_input.response_builder
                .speak(chores)
                .response
        )


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "What's up, dude?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can ask me for a fact or ask me what I think the clocks should play tonight."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GetRandomSportHandler())
sb.add_request_handler(GetRandomFactHandler())
sb.add_request_handler(GetTodaysChoresHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
