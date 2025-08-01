# Analytics Implementation Guide
## NSW Burns Community Survey Report

### Overview
This guide explains the comprehensive analytics implementation for the NSW Burns Community Survey report. The system tracks user engagement, interactions, and behavior patterns to understand how the community uses the survey data.

### What's Been Implemented

#### 1. Google Analytics 4 (GA4) Setup
- **Tracking ID**: G-B4V82DTKP6
- **Enhanced Configuration**: Custom parameters for detailed tracking
- **Custom Dimensions**: section_name, interaction_type, chart_name, persona_name

#### 2. Event Tracking Categories

##### Page Engagement
- `page_view`: Initial page load
- `section_view`: When users view different sections
- `scroll_depth`: Tracks 25%, 50%, 75%, 100% scroll completion
- `time_on_page`: Total time spent on page

##### Navigation
- `navigation_click`: When users click navigation links
- `mobile_menu_toggle`: Mobile menu usage

##### Data Visualization
- `chart_interaction`: Chart hover and interaction events
- `chart_name`: Specific chart being interacted with
- `interaction_type`: Type of interaction (hover, click, etc.)

##### Geographic Data
- `map_interaction`: Map-related interactions
- `marker_click`: When users click on LGA markers
- `center_marker_click`: Community center marker interactions

##### Persona Engagement
- `persona_view`: When users view persona details
- `persona_name`: Specific persona being viewed
- `modal_close`: Modal interaction tracking

### How to Access Analytics Data

#### 1. Google Analytics 4 Dashboard
1. Go to [Google Analytics](https://analytics.google.com)
2. Select your property (G-B4V82DTKP6)
3. Navigate to Reports > Engagement > Events

#### 2. Key Reports to Monitor

##### Real-Time Reports
- **Real-time**: See current visitors and their actions
- **Events**: Live event tracking

##### Engagement Reports
- **Pages and screens**: Most viewed sections
- **Events**: Custom event tracking
- **User engagement**: Time on page, scroll depth

##### Custom Reports
- **Section engagement**: Which sections are most popular
- **Chart interactions**: Which data visualizations are most engaging
- **Map usage**: Geographic data exploration patterns
- **Persona engagement**: Community interest in different personas

### Analytics Dashboard

A sample analytics dashboard (`analytics-dashboard.html`) has been created with:

#### Overview Metrics
- Total page views
- Unique visitors
- Average time on page
- Bounce rate

#### Engagement Analytics
- Section view counts
- Chart interaction patterns
- Map usage statistics
- Persona engagement rates

#### Technical Analytics
- Device types (desktop, mobile, tablet)
- Browser usage
- Geographic distribution of visitors

#### Real-time Activity
- Live visitor count
- Current activity monitoring

### Custom Dimensions and Metrics

#### Custom Dimensions
1. **section_name**: Which section users are viewing
2. **interaction_type**: Type of user interaction
3. **chart_name**: Specific chart being interacted with
4. **persona_name**: Persona being viewed

#### Custom Metrics
1. **scroll_depth**: How far users scroll
2. **time_spent_seconds**: Time on page
3. **respondent_count**: Number of respondents in clicked LGA
4. **total_respondents**: Total community size

### Event Categories

#### Engagement Events
- `section_view`: Section visibility tracking
- `scroll_depth`: Scroll behavior analysis
- `time_on_page`: Engagement duration

#### Navigation Events
- `navigation_click`: Menu navigation patterns
- `mobile_menu_toggle`: Mobile usage patterns

#### Data Visualization Events
- `chart_interaction`: Chart engagement tracking
- `chart_hover`: Hover behavior analysis

#### Geographic Events
- `map_interaction`: Map usage patterns
- `marker_click`: LGA interest tracking
- `center_marker_click`: Community center interest

#### Persona Events
- `persona_view`: Persona engagement
- `modal_interaction`: Modal usage patterns

### Implementation Details

#### JavaScript Functions
```javascript
// Core tracking function
function trackEvent(eventName, parameters = {})

// Section tracking
function trackSectionView(sectionName)

// Chart interaction tracking
function trackChartInteraction(chartName, interactionType)

// Persona tracking
function trackPersonaView(personaName)

// Map interaction tracking
function trackMapInteraction(interactionType, details = {})

// Scroll depth tracking
function trackScrollDepth()

// Time on page tracking
function trackTimeOnPage()
```

#### Automatic Tracking
- **Scroll depth**: Tracks at 25%, 50%, 75%, 100%
- **Section visibility**: Uses Intersection Observer API
- **Chart interactions**: Hover and click events
- **Map interactions**: Marker clicks and interactions
- **Modal interactions**: Persona modal usage

### Key Insights to Monitor

#### 1. Content Engagement
- Which sections are most viewed?
- How long do users spend on each section?
- What's the scroll depth pattern?

#### 2. Data Visualization Usage
- Which charts are most interacted with?
- Are users exploring the geographic data?
- How engaged are users with the personas?

#### 3. User Behavior
- Are users primarily on mobile or desktop?
- What's the geographic distribution of visitors?
- How do users navigate through the content?

#### 4. Community Interest
- Which LGAs are most clicked on the map?
- Which personas generate the most interest?
- What sections do users return to?

### Setting Up Custom Reports

#### 1. Section Engagement Report
1. Go to GA4 > Explore
2. Create new exploration
3. Add dimensions: section_name, event_name
4. Add metrics: event_count, user_engagement
5. Filter: event_name = "section_view"

#### 2. Chart Interaction Report
1. Create new exploration
2. Add dimensions: chart_name, interaction_type
3. Add metrics: event_count
4. Filter: event_name = "chart_interaction"

#### 3. Geographic Interest Report
1. Create new exploration
2. Add dimensions: lga_name, state
3. Add metrics: event_count, respondent_count
4. Filter: event_name = "marker_click"

### Privacy Considerations

#### Data Protection
- No personal information is collected
- All tracking is anonymous
- IP addresses are anonymized by Google Analytics
- Users can opt-out via browser settings

#### Compliance
- Analytics respect user privacy preferences
- No tracking of sensitive information
- Data is used only for community insights

### Troubleshooting

#### Common Issues
1. **Events not showing**: Check if gtag is loaded
2. **Custom dimensions missing**: Verify GA4 property settings
3. **Real-time data delayed**: Normal GA4 processing time

#### Debug Mode
```javascript
// Enable debug mode in browser console
gtag('config', 'G-B4V82DTKP6', {
  debug_mode: true
});
```

### Next Steps

#### 1. Monitor Initial Data
- Check real-time reports for first 24 hours
- Verify events are firing correctly
- Monitor for any technical issues

#### 2. Set Up Alerts
- Create custom alerts for unusual activity
- Set up weekly/monthly reports
- Monitor engagement trends

#### 3. Optimize Based on Data
- Identify most engaging content
- Improve less-viewed sections
- Enhance user experience based on patterns

### Contact Information
For technical support or questions about the analytics implementation, contact the development team.

---

*This analytics implementation provides comprehensive insights into how the NSW Burns community engages with the survey data, helping inform future community planning and event organization.* 