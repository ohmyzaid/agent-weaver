#ifndef CRAWLER_AGI_UTILITY_H
#define CRAWLER_AGI_UTILITY_H
namespace agent_weaver {
    inline float normalizeAngle(float angle) {
        while (angle > 180.0f) angle -= 360.0f;
        while (angle < -180.0f) angle += 360.0f;
        return angle;
    }
}
#endif
