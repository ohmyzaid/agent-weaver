#ifndef CRAWLER_AGI_CONTROLLER_HPP
#define CRAWLER_AGI_CONTROLLER_HPP
#include <cstddef>

namespace crawler_agi {
class Controller {
public:
    Controller();
    void init();
    void update(double dt);
    void setTarget(double target);
private:
    double current_value_;
    double target_value_;
};
}
#endif
