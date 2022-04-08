---
summary: A list of CSS classes used in Silk UI and OutSystems UI.
tags: 
en_title: 03 Migration reference tables for Silk and OutSystems Web UI
locale: en-us
guid: f3509fb6-8cae-449b-b321-1b7c828f48a8
---

# Migration reference tables for Silk and OutSystems Web UI

<div class="info" markdown="1">

This document is a work in progress.

</div>

This document is part of the migration path guide for customers of OutSystems 10 who want to continue developing their web application in OutSystems 11 Web UI Framework. Please refer to the table of content for the entire guide.

What follows is two sets of tables that show the CSS and pattern mappings between the  Silk Web UI and OutSytems Web UI. An empty cell means there is no corresponding pattern. The label "in progress" means that the item will be updated after we acquire the full technical details.

<div class="info" markdown="1">

The documents in this section:

* [Migrating UI of the Silk Web applications to OutSystems UI Framework](intro.md)
* [Migrating the patterns of the Silk web applications to OutSystems UI](migrate-patterns.md)
* [Migrating the structure of the Silk web applications to OutSystems UI](migrate-structure.md)
* [Migration reference tables for Silk and OutSystems Web UI](migration-reference-tables.md)

</div>

## CSS mapping

For a more straightforward migration process, we are keeping a fallback section with some of the rules that assist in preventing broken experience in older apps. We encourage you to use the new classes when building a new application or when migrating an application that is under development. This is to prevent a need for a migration process again in the future.

### Background colors

| Silk Web UI  | OutSystems Web UI |
| -------|------- | 
| Transparent | background-transparent
| White | background-neutral-0
| Silver | background-neutral-4
| Gray | background-neutral-7
| Black | background-neutral-10
| Yellow | background-yellow
| Red | background-red
| Plum | background-grape
| Green | background-green
| Turquoise | background-cyan
| Blue | background-blue
| DarkBlue | background-blue-darkest
| Orange | background-orange
| DarkRed | background-red-dark
| DarkPlum | background-grape-dark
| LightGreen | background-green-light

### Text colors

| Silk Web UI  | OutSystems Web UI |
| -------|------- |
Text_white | text-neutral-0
Text_orange | text-orange
Text_darkred | text-red-dark
Text_darkplum | text-grape-dark
Text_lightGreen | text-green-light
Text_silver | text-neutral-4
Text_black | text-neutral-10
Text_yellow | text-yellow
Text_red | text-red
Text_plum | text-grape
Text_green | text-green
Text_turquoise | text-cyan
Text_darkblue | text-blue-dark
Text_gray | text-neutral-7


### Buttons

| Silk Web UI  | OutSystems Web UI |
| -------|------- |
Button Is_Default | btn background-primary
Button Success | btn background-success
Button Danger | btn background-error
Button Small | btn font-size-xs


### Text


| Silk Web UI  | OutSystems Web UI |
| -------|------- |
| Heading1 | heading1
| Heading2 | heading2
| Heading3 | heading3
| Heading4 | heading4
| Bold | font-bold
| Italic | 
| Underline | 
| Text_Error | text-error
| Text_note | font-size-xs text-neutral-7
| Text_large | heading6
| Text_uppercase | text-uppercase

### Right to left


| Silk Web UI  | OutSystems Web UI |
| -------|------- |
| AR | is-rtl


### Image style

| Silk Web UI  | OutSystems Web UI |
| -------|------- |
| .Image_circle | border-radius-circle
| .Image_rounded | border-radius-rounded


## Pattern mappings

The following tables list the patterns in the OutSystems Web UI Framework and the corresponding patterns in the Silk Web UI Framework.

### Content

| Silk Web UI  | OutSystems Web UI |
| -------|------- |
Accordion | Accordion
Accordion3Items | 
Accordion4Items | 
Accordion5Items | 
AccordionItem | AccordionItem
Alert | Alert
| | Animate (in preparation) 
Balloon | Balloon
BalloonFooter | 
BlankSlate | BlankSlate
Box | 
Bullets | (in preparation)
ButtonsArea | 
| | Card
CardBackground | CardBackground
| | CardSectioned
CardLeftImage | 
CardSimple | 
CardSimpleImage | 
Carousel | (in preparation)
| | FloatingActions (in preparation)
| | FlipContent (in preparation)
Info | 
LightBoxImage | (in preparation)
Modal | Modal
Panel | Panel
Post | (in preparation)
Section | Section
| | SectionIndex (in preparation)
SectionExandable | 
Separator | (in Utilities)
| | Tag
Tooltip | Tooltip
TooltipClass | 
TooltipContainer | 

### Controls

| Silk Web UI | OutSystems Web UI |
| -------|------- |
| | AnimatedLabel
ButtonDropdown | 
| | ButtonGroup
ButtonGroup2 | 
ButtonGroup3 | 
ButtonGroup4 | 
ButtonGroup5 | 
| | ButtonGroupItem
Calendar | 
| | DatePicker
| | TimePicker (in preparation)
| | Dropdown
| | DropdownSelect
FileUpload | FileUpload
| | FloatingActions (in preparation)
IconDropdown | 
InlineDropdown | 
InputWithIcons | InputWithIcon
RangeSlider | RangeSlider
| | RangeSliderInterval
Search | Search
Select2 | 
| | SearchBalloon
| | Stepper (in preparation)
ToggleButton | ToggleButton
Video | (in preparation)

### Data

| Silk Web UI | OutSystems Web UI |
| -------|------- |
Badge | Badge
Counter | Counter
IconBadge | IconBadge
Progressbar | Progressbar
| | ProgressCircle (in preparation)
TileIcon | 
TileIconText | 
TileNumber | 
UserInitials | UserInitials

### Development

| Silk Web UI | OutSystems Web UI |
| -------|------- |
CSS | 
HTML | 
jQuery | 
JS | 

### Email

| Silk Web UI | OutSystems Web UI |
| -------|------- |
Email3Rows | 
EmailSection | 
LayoutEmail | 

### Layout

| Silk Web UI | OutSystems Web UI |
| -------|------- |
LayoutLogin | LayoutLogin
| | LayoutLoginSplit
| | LayoutMenuSide
| | LayoutMenuTop
LayoutPopup | LayoutPopup
| | LayoutSimple
| | LayoutForm
WidgetsForLayout | 

### Navigation

| Silk Web UI | OutSystems Web UI |
| -------|------- |
Breadcrumbs | Breadcrumbs
| | BreadcrumbsItem
NavigationBar | 
SectionIndex | 
| | Sidebar
Tabs | Tabs
| | TabsContentItem
| | TabsHeaderItem
Wizard | Wizard
Wizard3Steps | 
Wizard4Steps | 
Wizard5Steps | 
WizardStep | WizardItem 

### Responsive

| Silk Web UI | OutSystems Web UI |
| -------|------- |
DisplayOnDevice | (in preparation)
LoadOnVisible | (in preparation)
MoveOnDevice | (in preparation)
ResponsiveImages | 
ResponsiveTableRecords | 
ToggleOnDevice | 

### Structure

| Silk Web UI | OutSystems Web UI |
| -------|------- |
(VerticalAlign in Utilities) | AlignCenter
Columns2 | Columns2 
Columns3 | Columns3
Columns4 | Columns4
Columns5 | Columns5
Columns6 | Columns6
Gallery | Gallery
MediumLeftColumn | ColumnsMediumLeft
MediumRightColumn | ColumnsMediumRight
SmallLeftColumn | ColumnsSmallLeft
SmallRightColumn | ColumnsSmallRight

### Utilities

| Silk Web UI | OutSystems Web UI |
| -------|------- |
CharacterCount | (in preparation)
FeedbackAjaxWait | 
Fieldset | (in preparation)
FlipContent | 
Iframe | (in preparation)
ScrollToElement | (in preparation)
StackedIcon | (in preparation)
| (in Content) | Separator
VerticalAlign | (AlignCenter in Structure)
