#ifndef CRAWLER_AGI_PID_CONTROL_H
#define CRAWLER_AGI_PID_CONTROL_H

namespace agent_weaver {
class PIDController {
public:
    PIDController();
    void reset();
    float compute(float setpoint, float measured, float dt);
};
}
#endif
