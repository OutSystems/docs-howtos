---
tags: time-zones
summary: OutSystems 11 (O11) defaults to local user time for apps and uses UTC across all cloud servers, with synchronization recommended.
guid: 5e9d4c5c-4d06-4102-91e9-bcbc7350e8fd
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# How to time zones work in OutSystems and how can I change them?

How do time zones work in OutSystems?

## How are time zones determined in OutSystems and how can they be manipulated if needed?

How are time zones determined in OutSystems and how can they be manipulated if needed?

## OutSystems Time Zones

By default, for Reactive and mobile applications, OutSystems will represent the datetime variables in the user's timezone (where user's device is located).

In an OutSystems Platform environment the database, controller and all front-ends are required to be in the same timezone.

The rationale for this is to ensure a simpler mental model for both developers and operators. If the time is consistent across the environment, it's easier for all to understand when time-dependent events (timers, BPT) are supposed to occur. This also makes programming with times simpler as the developer does not need to do complicated code to normalize timestamps in their applications.

In addition to being in the same timezone, OutSystems also recommends that all parts of an environment be synchronized in terms of time. Time drifts greater than a few seconds can lead to unexpected behavior. It is recommended by OutSystems that customers sync all their front-ends and database with the same NTP time server.

In the OutSystems Cloud all servers are set to work in the UTC time zone. This configuration cannot be changed.

Applications that need to deal with time zone differences from UTC need to consider that from the early phases of development.

## Controlling Time Zones

As an example, the [CurrDateTime](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Logic/Built-in_Functions/Date_and_Time#CurrDateTime) function returns a time zone specific to the situation in which it is utilized.

In client-side calls, it returns the device time.
In server-side calls, it returns the platform server time.
In query calls, it returns the platform server time.

Date times in the device are converted in the server to the server time zone.
Conversely, date times in the server are converted in the device to the device time zone.

Once you know this, it's a matter of displaying the time in the timezone of your choice.
You can use a forge component to facilitate the conversion upon saving or displaying the timestamps.  [TimezoneReactiveUtils](https://www.outsystems.com/forge/component-overview/2199/timezonereactiveutils) is an example of this, and while it is not supported by OutSystems, it should provide output parameters to convert times based on time zones set by the developer.

